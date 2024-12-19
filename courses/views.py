from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from .models import Course, CounselingRequest, Enrollment

# Home View
def home(request):
    return render(request, 'home.html')

# List all Courses
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

# Course Detail View with Enrollment
@login_required
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)

    if request.method == 'POST':  # Handle Enrollment Form Submission
        Enrollment.objects.get_or_create(user=request.user, course=course)
        return redirect('enrolled_courses')

    return render(request, 'courses/course_detail.html', {'course': course})

# View Enrolled Courses
@login_required
def enrolled_courses(request):
    enrollments = Enrollment.objects.filter(user=request.user)
    return render(request, 'courses/enrolled_courses.html', {'enrollments': enrollments})

# Counseling Form View
@login_required
def counseling_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save form data
        CounselingRequest.objects.create(name=name, email=email, message=message)
        return redirect('counseling_success')

    return render(request, 'counseling_form.html')

# Counseling Success View
def counseling_success(request):
    return render(request, 'counseling_success.html')

# Counseling Requests Admin View
@user_passes_test(lambda u: u.is_staff)  # Allow only staff/admins to access
def counseling_requests_list(request):
    requests = CounselingRequest.objects.all()
    return render(request, 'counseling_requests.html', {'requests': requests})

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
