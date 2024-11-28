from django .urls import path
from . import views

urlpatterns = [
    path('' , views.homePage , name='home'),
    
    path('hr_dashboard/' , views.hrDashboardPage , name='hr_dashboard'),
    path('employee_dashboard/' , views.employeeDashboardPage , name='employee_dashboard'),
    path('signup/' , views.signUpPage , name='signup'),
    path('login/' , views.loginPage , name='login'),
    path('logout/' , views.logoutPage , name='logout'),
    path('hr/addemployee/' , views.addEmployeePage , name='hr_addemployee'),
    path('hr/employeedetails/' , views.employeeDetailsPage , name='hr_employee_details'),
    path('hr/employeedetails/deleteemployee/<int:id>',views.deleteEmployee),
    path('hr/employeedetails/editemployee/<int:id>',views.editEmployee, name='hr_edit_employee'),
    path('do-edit-employee/<int:id>/', views.doEditEmployee, name='do-edit-employee'),

    path('employee/addattendance/' , views.employeeaddAttendancePage , name = 'employee_addattendance'),
    # path('hr/addattendance/' , views.hraddAttendancePage , name = 'hr_addattendance'),
    path('hr/attendancedetails/' , views.attendanceDetailsPage , name = 'hr_attendance_details'),
    path('hr/attendancedetails/deleteattendance/<int:id>',views.deleteAttendance),

    path('hr/attendancedetails/editattendance/<int:id>',views.editAttendance , name='hr_edit_attendance'),
    path('do_editattendance/<int:id>/', views.doEditAttendance, name='do_edit_attendance'),

    path('employee/applyleave/' , views.applyForLeavePage , name = 'employee_applyleave'),
    path('hr/applyleavedetails/' , views.LeaveDetailsPage , name = 'hr_apply_leave_details'),

    path('hr/applyleavedetails/editleave/<int:id>/', views.editLeave, name='hr_edit_leave'),
    path('do_edit_leave/<int:id>/', views.doEditLeave, name='do_edit_leave'),
    path('hr/approveleave/', views.approveLeavePage, name='hr_approve_leave'),
    
    path('hr/applyleavedetails/deleteleave/<int:id>',views.deleteLeave),
    # path('leavedetails/editleave/<int:id>',views.editAttendance),
    # path('do_editattendance/<int:id>',views.doEditAttendance),
    
    
    # path('qr-code/<int:employee_id>/', views.generate_qr_code, name='generate_qr_code'),
    # path('attendance/<int:employee_id>/', views.attendance_form, name='attendance_form'),
    # path('mark-attendance/', views.mark_attendance, name='mark_attendance'),
    
    
    # path('generate_qr_code/<int:employee_id>/', views.generate_qr_code, name='generate_qr_code'),

    path('generate_qr/' , views.generateQrPage , name='generate_qr'),
    
   
]
