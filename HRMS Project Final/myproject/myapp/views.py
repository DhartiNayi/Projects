from django.shortcuts import render , HttpResponse , redirect ,  get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from myapp.models import *
from .models import CustomUser
from django.urls import reverse
from django.contrib.auth import get_user_model

import qrcode
from io import BytesIO

# Create your views here.

@login_required(login_url = 'login')
def homePage(request):
    return render(request , "hr/home.html")

# Qr code 
@login_required(login_url = 'login')
def generateQrPage(request):
    return render(request , "generate_qr.html")    

@login_required(login_url = 'login')
def dashboardPage(request):
    return render(request , "dashboard.html")    


# def signUpPage(request):
#     if request.method == 'POST':
#         sname = request.POST.get('username') 
#         semail = request.POST.get('email') 
#         spassword1 = request.POST.get('password') 
#         spassword2 = request.POST.get('confirm-password') 

#         if spassword1 != spassword2:
#             return JsonResponse({'error': 'Your Password and confirmation password are not the same!'}, status=400)  # Return error JSON response
#         else:
#             my_user = User.objects.create_user(sname, semail, spassword1)
#             my_user.save()
#             return JsonResponse({'redirect_url': '/login/'})  # Return JSON response for redirecting to login page

# def signUpPage(request):
#     if request.method == 'POST':
#         sname = request.POST.get('username') 
#         semail = request.POST.get('email') 
#         spassword1 = request.POST.get('password') 
#         spassword2 = request.POST.get('confirm-password') 

#         if spassword1 != spassword2:
#             messages.info(request, "Your password and confirmation password do not match!")
#             return JsonResponse({'error': 'Password mismatch'}, status=400)  

#         if User.objects.filter(username=sname).exists() or User.objects.filter(email=semail).exists():
#             messages.info(request, "User with the same username or email already exists!")
#             return JsonResponse({'error': 'User already exists'}, status=400) 

#         my_user = User.objects.create_user(sname, semail, spassword1)
#         my_user.save()
#         return JsonResponse({'redirect_url': '/login/'})  

    
#     return render(request, "signup.html")


# def loginPage(request):
#     if request.method == "POST":
#         lname = request.POST.get('username') 
#         lpassword = request.POST.get('password') 

#         user = authenticate(request, username=lname, password=lpassword)

#         if user is not None:
#             login(request, user)
#             return JsonResponse({'redirect_url': '/dashboard/'})  # Redirect to dashboard upon successful login
#         else:
#             messages.info(request, "Username or password is incorrect!")
#             return JsonResponse({'error': 'Username or password is incorrect!'}, status=400)  # Return error message

    
#     return render(request, "login.html")

# def logoutPage(request):
#     logout(request)
#     # return JsonResponse({'redirect_url': '/signup/'})  
#     return redirect('login')

# def signUpPage(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         role = request.POST.get('role')

#         if CustomUser.objects.filter(username=username).exists():
#             return JsonResponse({'error': 'User with this username already exists'}, status=400)

#         user = CustomUser.objects.create_user(username=username, password=password,role=role)
#         # return JsonResponse({'redirect_url': reverse('login')})
#         return redirect("login")
#     return render(request, "signup.html")

CustomUser = get_user_model()

def signUpPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')
        role = request.POST.get('role')

        if password != confirm_password:
            messages.info(request, "Your password and confirmation password do not match!")
            return JsonResponse({'error': 'Password mismatch'}, status=400)

        if CustomUser.objects.filter(username=username).exists():
            messages.info(request, "User with the same username already exists!")
            return JsonResponse({'error': 'User already exists'}, status=400)

        user = CustomUser.objects.create_user(username=username, password=password, role=role)
        user.save()
        return JsonResponse({'redirect_url': '/login/'})

    return render(request, "signup.html")

# def loginPage(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             if user.role == 'HR':
#                 # return JsonResponse({'redirect_url': reverse('hr_dashboard')})
#                 return redirect("hr_dashboard")
#             else:
#                 # return JsonResponse({'redirect_url': reverse('employee_dashboard')})
#                 return redirect("employee_dashboard")
#         else:
#             return JsonResponse({'error': 'Invalid username or password'}, status=400)

#     return render(request, "login.html")

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.role == 'HR':
                return JsonResponse({'redirect_url': '/hr_dashboard/'})  # Redirect to HR dashboard upon successful login
            else:
                return JsonResponse({'redirect_url': '/employee_dashboard/'})  # Redirect to Employee dashboard upon successful login
        else:
            messages.info(request, "Username or password is incorrect!")
            return JsonResponse({'error': 'Invalid username or password'}, status=400)  # Return error message

    return render(request, "login.html")

@login_required
def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required
def hrDashboardPage(request):
    if request.user.role != 'HR':
        return redirect('employee_dashboard')
    return render(request, "hr/hr_dashboard.html")

@login_required
def employeeDashboardPage(request):
    if request.user.role != 'Employee':
        return redirect('hr_dashboard')
    return render(request, "employee/employee_dashboard.html")


@login_required(login_url = 'login')
def addEmployeePage(request):

    if request.method == "POST":
       
        name = request.POST.get("name")
        designation = request.POST.get("designation")
        email = request.POST.get("email")
        phone_no = request.POST.get("phone")
        joining_date = request.POST.get("joining_date")
        
        
        employee = Employee.objects.create(
            name=name,
            designation=designation,
            email=email,
            phone_no=phone_no,
            joining_date=joining_date,
        )

        return JsonResponse({'success': True, 'message': 'Employee added successfully.'})
    elif request.method == "GET":
        return render(request, "hr/add_employee.html", {})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method.'})

@login_required(login_url = 'login')        
def employeeDetailsPage(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        employee_data = list(employees.values())
        
        if request.headers.get('Accept') == 'application/json':
            return JsonResponse({'employees': employee_data})
        else:
            return render(request, "hr/employee_details.html", {'employees': employees})

@login_required(login_url = 'login')
def deleteEmployee(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()

    return redirect("employee_details")

@login_required(login_url = 'login')
def editEmployee(request, id):
    employee = get_object_or_404(Employee, pk=id)
    return render(request, 'hr/edit_employee.html', {'employee': employee})
    
    # return JsonResponse({'edit_emp': {
    #     'id': employee.id,
    #     'name': employee.name,
    #     'designation': employee.designation,
    #     'email': employee.email,
    #     'phone_no': employee.phone_no,
    #     'joining_date': str(employee.joining_date)
    # }})
    
   
@login_required(login_url = 'login')
def doEditEmployee(request, id):
    if request.method == "POST":
        
        print("POST request received")
        print("Received data:", request.POST)
        
        name = request.POST.get("name")
        designation = request.POST.get("designation")
        email = request.POST.get("email")
        phone_no = request.POST.get("phone_no")
        joining_date = request.POST.get("joining_date")
        employee = get_object_or_404(Employee, pk=id)

        # Update employee fields
        employee.name = name
        employee.designation = designation
        employee.email = email
        employee.phone_no = phone_no
        employee.joining_date = joining_date

        employee.save()

        return JsonResponse({'success': True, 'message': 'Employee updated successfully.'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)

@login_required(login_url = 'login')
def employeeaddAttendancePage(request):
    if request.method == "POST":
        employee_name = request.POST.get("employee")
        # designation = request.POST.get("designation")
        date = request.POST.get("date")
        check_in = request.POST.get("check-in")
        check_out = request.POST.get("check-out")
        # manually_updated = request.POST.get("manually-updated", False)

        try:
            matching_employees = Employee.objects.filter(name=employee_name)
            if matching_employees.exists():
                employee = matching_employees.first()
                attendance = EmployeeAttendance(
                    employee=employee,
                    # designation=designation,
                    date=date,
                    check_in=check_in,
                    check_out=check_out,
                    # manually_updated=manually_updated
                )
                attendance.save()
                return JsonResponse({'success': True, 'message': 'Attendance added successfully.'})
            else:
                return JsonResponse({'success': False, 'message': 'Employee does not exist!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return render(request, 'employee/add_attendance.html', {})

# @login_required(login_url = 'login')
# def hraddAttendancePage(request):
#     if request.method == "POST":
#         employee_name = request.POST.get("employee")
#         # designation = request.POST.get("designation")
#         date = request.POST.get("date")
#         check_in = request.POST.get("check-in")
#         check_out = request.POST.get("check-out")
#         # manually_updated = request.POST.get("manually-updated", False)

#         try:
#             matching_employees = Employee.objects.filter(name=employee_name)
#             if matching_employees.exists():
#                 employee = matching_employees.first()
#                 attendance = EmployeeAttendance(
#                     employee=employee,
#                     # designation=designation,
#                     date=date,
#                     check_in=check_in,
#                     check_out=check_out,
#                     # manually_updated=manually_updated
#                 )
#                 attendance.save()
#                 return JsonResponse({'success': True, 'message': 'Attendance added successfully.'})
#             else:
#                 return JsonResponse({'success': False, 'message': 'Employee does not exist!'})
#         except Exception as e:
#             return JsonResponse({'success': False, 'message': str(e)})
#     return render(request, 'hr/add_attendance.html', {})

@login_required(login_url = 'login')
def attendanceDetailsPage(request):
    if request.method == 'GET':
        attendance = EmployeeAttendance.objects.all()
        attendance_data = list(attendance.values())
        
        if request.headers.get('Accept') == 'application/json':
            return JsonResponse({'attendance': attendance_data})
        else:
            return render(request, "hr/attendance_details.html", {'attendance': attendance})

@login_required(login_url = 'login')
def deleteAttendance(request,id):
    delete_attendance = EmployeeAttendance.objects.get(pk=id)
    delete_attendance.delete()

    return redirect("attendance_details")    

# @login_required(login_url = 'login')
# def editAttendance(request,id):

#     edit_atd = EmployeeAttendance.objects.get(pk=id)

#     return render(request ,"edit_attendance.html" , {'edit_atd' :  edit_atd})    
 

# @login_required(login_url = 'login')
# def doEditAttendance(request, id):
#     if request.method == "POST":
#         employee_name = request.POST.get("name")
#         date = request.POST.get("date")
#         check_in = request.POST.get("check_in")
#         check_out = request.POST.get("check_out")
#         # manually_updated = request.POST.get("manually_updated", False)

#         try:
#             edit_atd = EmployeeAttendance.objects.get(pk=id)
#             edit_atd.employee_name = employee_name
#             edit_atd.date = date
#             edit_atd.check_in = check_in
#             edit_atd.check_out = check_out
#             # edit_atd.manually_updated = manually_updated
#             edit_atd.save()

#             return JsonResponse({'success': True, 'message': 'Attendance updated successfully.'})
#         except EmployeeAttendance.DoesNotExist:
#             return JsonResponse({'success': False, 'message': 'Attendance not found.'}, status=404)
#     else:
#         return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)
    

@login_required(login_url='login')
def editAttendance(request, id):
    edit_atd = get_object_or_404(EmployeeAttendance, pk=id)
    return render(request, 'hr/edit_attendance.html', {'edit_atd': edit_atd})

@login_required(login_url='login')
def doEditAttendance(request, id):
    if request.method == "POST":
        employee = request.POST.get("employee")
        date = request.POST.get("date")
        check_in = request.POST.get("check_in")
        check_out = request.POST.get("check_out")

        

        try:
            attendance = get_object_or_404(EmployeeAttendance, pk=id)
            attendance.employee.name = employee
            attendance.date = date
            attendance.check_in = check_in
            attendance.check_out = check_out
            attendance.save()

            print("after save")

            return JsonResponse({'success': True, 'message': 'Attendance updated successfully.'})
        except EmployeeAttendance.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Attendance not found.'}, status=404)
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)


@login_required(login_url = 'login')
def applyForLeavePage(request):
    if request.method == "POST":
        employee_name = request.POST.get("name")
        designation = request.POST.get('designation')
        leave_type = request.POST.get("leave-type")  
        duration = request.POST.get("duration")
        start_date = request.POST.get("start-date")
        end_date = request.POST.get("end-date")
        
        # print(f"leave_type: {leave_type}")
        print(request.POST)

        try:
            matching_employees = Employee.objects.filter(name=employee_name)
            if matching_employees.exists():
                employee = matching_employees.first()
                apply_leave = EmployeeLeave(
                    employee=employee,
                    designation=designation,
                    leave_type=leave_type,
                    duration=duration,
                    start_date=start_date,
                    end_date=end_date
                )
                apply_leave.save()
                return JsonResponse({'success': True ,'message': 'Leave application submitted successfully.'})
            else:
                return JsonResponse({'success': False, 'message': 'Employee does not exist.'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})

    return render(request, "employee/leave_apply.html", {})

@login_required(login_url = 'login')
def LeaveDetailsPage(request):
    if request.method == 'GET':
        apply_leave = EmployeeLeave.objects.all()
        leave_data = list(apply_leave.values())
        
        if request.headers.get('Accept') == 'application/json':
            return JsonResponse({'apply_leave': leave_data})
        else:
            return render(request, "hr/applyleave_details.html", {'apply_leave': apply_leave})

@login_required(login_url='login')
def editLeave(request, id):
    leave = get_object_or_404(EmployeeLeave, pk=id)
    return render(request, 'hr/edit_leave.html', {'leave': leave, 'employee_name': leave.employee.name})

@login_required(login_url='login')
def doEditLeave(request, id):
    if request.method == "POST":
        leave = get_object_or_404(EmployeeLeave, pk=id)

        leave.employee.name = request.POST.get("employee_name")
        leave.designation = request.POST.get("designation")
        leave.leave_type = request.POST.get("leave-type")
        leave.duration = request.POST.get("duration")
        leave.start_date = request.POST.get("start-date")
        leave.end_date = request.POST.get("end-date")

        leave.save()

        return JsonResponse({'success': True, 'message': 'Leave updated successfully.'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)            

@login_required(login_url = 'login')
def deleteLeave(request,id):
    delete_leave = EmployeeLeave.objects.get(pk=id)
    delete_leave.delete()

    return redirect("apply_leave_details")    

@login_required(login_url = 'login')
def approveLeavePage(request):
    return render(request , "hr/approve_leave.html") 



@login_required(login_url='login')
def attendance_page(request, user_id):
    user = get_object_or_404(User, id=user_id)

    current_user = request.user
    user_id = current_user.id
    # print(user_id)
    return render(request, 'employee/add_attendance.html', {'user_id': user_id})


 