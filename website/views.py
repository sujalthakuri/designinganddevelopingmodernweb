from django.shortcuts import render, redirect
from django.http import HttpResponse
from. models import Users
from. models import image
from. models import admin
from. models import follow
from website.authenticate import Authenticate
from django.contrib import messages
from django.contrib.auth import logout as django_logout
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.core.paginator import Paginator

def index(request):
	if(request.session['username']!=None):
		return redirect('/home/')
	return render(request,'website/index.html')

## Checking input data to login in Admin
def admin_login(request):
	admin_n = request.session['adminname'] = request.POST['adminname']
	password = request.POST['password']

	try:
		admind = admin.objects.get(adminname = admin_n)

		if(admind.password!= password):
			messages.warning(request,'Password dont match')
			return redirect('/')
		

	except:
		messages.warning(request,'Admin Name dont match')
		return redirect("/")
	return redirect('/dashboard/')

## To Show Notification of new user following the Active User
def notification(request):
	follower = follow.objects.all().filter(profile_id = request.session['user_id'])
	followed = Users.objects.all().filter(user_id__in = follower.values('user_id'))
	return render(request,"website/notification.html",{'users':followed})

## Shows Users that follow the Active or Logged in User
def followers(request):

	follower = follow.objects.all().filter(profile_id = request.session['user_id'])
	followed = Users.objects.all().filter(user_id__in = follower.values('user_id'))
	return render(request,"website/followed.html/",{'users':followed})

## Shows Users the Active or Logged in User follows
def following(request):
	followers = follow.objects.all().filter(user_id = request.session['user_id'])
	followed = Users.objects.all().filter(user_id__in=followers.values('profile_id'))
	return render(request,"website/following.html",{'users':followed})



## Admin Dashboard
def dashboard(request):
	users = Users.objects.all()
	paginator = Paginator(users, 2)
	page = request.GET.get('page')
	users = paginator.get_page(page)

	admind = request.session['adminname']
	return render(request,'website/admin.html/',{'users':users,'admin':admind})

## Admin Dashboard updating the data of the Users
def update(request):
	user_id = request.POST.get('user_id')
	fname = request.POST.get('fname')
	lname = request.POST.get('lname')
	username = request.POST.get('username')
	email = request.POST.get('email')
	bio = request.POST.get('bio')
	password = request.POST.get('password')

	users = Users.objects.get(user_id = user_id)

	users.fname = fname
	users.lname = lname 
	users.username = username
	users.email = email
	users.bio = bio
	users.password = password
	users.save()
	return redirect('/dashboard/')


## User Signing up
def signup(request):
	fname = request.POST.get('fname')
	lname = request.POST.get('lname')
	username = request.POST.get('username')
	email = request.POST.get('email')
	password = request.POST.get('password')
	image = 'avatar.jpg'
	if(Users.objects.filter(username = username).exists()):
		messages.warning(request,'Username Already Exists!')
		return redirect('/')

	signup_details = Users(fname = fname, lname = lname, username = username, email = email, password = password, image = image)
	signup_details.save()

	return render(request, "website/signup.html")

## User Loggin In
def login(request):
	usern = request.POST['username']
	passw = request.POST['password']

	try:
		user = Users.objects.get(username = usern)


		if(user.password!=passw):
			messages.warning(request,'Password Do Not match')
			return redirect('/')

	except:
		messages.warning(request,'Username Do Not match')
		return redirect('/')
	
	user = Users.objects.get(username = usern)
	request.session['username'] = usern
	request.session['user_id'] = user.user_id		
	user_pass = Users.objects.all()

	return redirect('/home/',{'users':user_pass,})
	# return render(request,'website/home.html',{'users':user_pass,})

##Checking if the User is Logged in
## Retrieves the Active or Logged in User data From the Database
@Authenticate.auth_user
def profile(request):
	user = Users.objects.get(username = request.session['username'])
	context = {'user': user}
	image_show = image.objects.all().filter(user_id = user.user_id)
	follower = follow.objects.all().filter(profile_id = request.session['user_id'])
	followed = Users.objects.all().filter(user_id__in = follower.values('user_id')).count()
	followers = follow.objects.all().filter(user_id = request.session['user_id'])
	following = Users.objects.all().filter(user_id__in=followers.values('profile_id')).count()
	context = {'user': user,'image_show':image_show,'follower':followed,'following':following}



	return render(request, 'website/profile.html',context)

##Checking if the User is Logged in
## Uploading the User Profile Picture
@Authenticate.auth_user
def upload(request):  
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        user = Users.objects.get(username = request.session['username'])
        user_id = user.user_id
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        p_image = Users.objects.get(user_id = user_id)
        p_image.image = myfile.name
        p_image.save()

        return redirect('/profile/')
    # return render(request, '/login/')

##Checking if the User is Logged in
## Uploading Photos for the user    
@Authenticate.auth_user
def upload_photo(request):
	if request.method == 'POST' and request.FILES['myfile']:
		myfile = request.FILES['myfile']
		user = Users.objects.get(username = request.session['username'])
		user_id = user.user_id
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		u_image = image(image = myfile.name,user_id = user_id)
		u_image.save()
		return redirect('/profile/')

## Updating Bio for the active User
@Authenticate.auth_user
def bio(request):
	username = request.session['username']
	bio_text = request.POST['bio']
	bio = Users.objects.get(username = username)
	bio.bio = bio_text
	bio.save()

	return redirect('/profile/')

##Shows data of the Profile the user has clicked on
def userprofile(request,user_id):
	if(request.session['username']!= None):
		count = 0
		usern = user_id
		profile_user = Users.objects.get(user_id = user_id)
		image_user = image.objects.all().filter(user_id = profile_user.user_id)
		followed = follow.objects.all().filter(user_id = request.session['user_id'])
		followers = follow.objects.all().filter(user_id = usern)
		following = Users.objects.all().filter(user_id__in=followers.values('profile_id')).count()
		followe = follow.objects.all().filter(profile_id = user_id)
		follower = Users.objects.all().filter(user_id__in = followe.values('user_id')).count()
		for f in followed:
			if(f.profile_id == user_id):
				count = count + 1

		if count >0:
			return render(request,'website/userprofile.html',{'user':profile_user,'image_user':image_user,'followed': 'Followed','follower':follower,'following':following})
		else:
			return render(request,'website/userprofile.html',{'user':profile_user,'image_user':image_user,'follower':follower,'following':following})
	else:
		messages.warning(request,"Please Login...")
		return redirect('/')

## Executed when Following a new User
@Authenticate.auth_user
def follow_user(request):
	userid = request.POST['user_id']
	profileid = request.POST['profile_id']


	followuser = follow(user_id = userid, profile_id = profileid)
	followuser.save()
	return redirect("/home/")

def success(request): 
    return HttpResponse('successfully uploaded') 


## Editing the User data by The Admin Dashboard
def edit(request,id):
	user=Users.objects.get(user_id=id)
	
	return render(request,'website/edit.html',{'users':user})

## Deleting the User data by The Admin Dashboard
def delete(request,id):
	user = Users.objects.get(user_id = id)
	user.delete()
	return redirect("/dashboard/")

## Searching for Users in the Website
@Authenticate.auth_user
def search(request):
    if request.method == 'GET':
        query= request.GET.get('search')

        if query is not None:
            lookups= Q(fname__icontains=query) | Q(lname__icontains=query)

            results= Users.objects.exclude(user_id= request.session['user_id']).filter(lookups).distinct()

            return render(request, 'website/search.html/', {'results': results})

        else:
            return render(request, 'website/search.html/')

    else:
        return render(request, 'website/search.html/')

## Displays all the Users of the Website except the Logged in User
## First Page of the Website after logging in
@Authenticate.auth_user
def home(request):
	user = Users.objects.exclude(username = request.session['username'])
	return render(request, 'website/home.html',{'users':user})

## Logouts clearing all the Sessions of the Logged In User
def logout(request):
    django_logout(request)

    request.session['adminname'] = None
    request.session['username'] = None
    return redirect('/')

