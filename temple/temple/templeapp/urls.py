from django.urls import path

from templeapp import views

urlpatterns=[
    path('',views.index,name='index'),
    path('login1', views.login1, name='login1'),

    #admin
    path('add_video',views.add_video,name='add_video'),
    path('mng_committee',views.mng_committee,name='mng_committee'),
    path('add_mng_committee',views.add_mng_committee,name='add_mng_committee'),
    path('add_mng_auditorium', views.add_mng_auditorium, name='add_mng_auditorium'),
    path('tmp_pgm_page', views.tmp_pgm_page, name='tmp_pgm_page'),
    path('add_tmp_pgm_page', views.add_tmp_pgm_page, name='add_tmp_pgm_page'),
    path('admin_view_videos', views.admin_view_videos, name='admin_view_videos'),
    path('admin_home', views.admin_home, name='admin_home'),
    path('manage_auditorium', views.manage_auditorium, name='manage_auditorium'),
    path('user_manage', views.user_manage, name='user_manage'),
    path('mng_aud_booking', views.mng_aud_booking, name='mng_aud_booking'),
    path('view_verified_booking',views.view_verified_booking,name='view_verified_booking'),
    path('view_user_manage', views.view_user_manage, name='view_user_manage'),
    path('view_reports_auditorium', views.view_reports_auditorium, name='view_reports_auditorium'),
    path('view_reports_auditorium1', views.view_reports_auditorium1, name='view_reports_auditorium1'),
    path('view_add_committee', views.view_add_committee, name='view_add_committee'),
    path('view_add_committee', views.view_add_committee, name='view_add_committee'),
    path('view_add_pgm', views.view_add_pgm, name='view_add_pgm'),
    path('view_manage_aud', views.view_manage_aud, name='view_manage_aud'),
    path('aud_bill_generate/<int:id>',views.aud_bill_generate,name='aud_bill_generate'),
    path('aud_bill_generate1/<int:id>', views.aud_bill_generate1, name='aud_bill_generate1'),

    #committee
    path('about_chitti', views.about_chitti, name='about_chitti'),
    path('add_about_chitti', views.add_about_chitti, name='add_about_chitti'),
    path('cm_add_pgms', views.cm_add_pgms, name='cm_add_pgms'),
    path('chitti_details_mbr', views.chitti_details_mbr, name='chitti_details_mbr'),
    path('committee_home', views.committee_home, name='committee_home'),
    path('committee_pgms', views.committee_pgms, name='committee_pgms'),
    path('cm_select_winners', views.cm_select_winners, name='cm_select_winners'),
    path('verified_members', views.verified_members, name='verified_members'),
    path('verify_members', views.verify_members, name='verify_members'),
    path('cm_view_about_chitti', views.cm_view_about_chitti, name='cm_view_about_chitti'),
    path('cm_view_add_pgms', views.cm_view_add_pgms, name='cm_view_add_pgms'),
    path('cm_view_payed_chitti', views.cm_view_payed_chitti, name='cm_view_payed_chitti'),

    path('cm_view_payed_chitti1', views.cm_view_payed_chitti1, name='cm_view_payed_chitti1'),
    path('cm_view_payed_chitti2/<int:id>', views.cm_view_payed_chitti2, name='cm_view_payed_chitti2'),

    path('cm_view_selected_winners', views.cm_view_selected_winners, name='cm_view_selected_winners'),
    path('cm_view_temple_pgm', views.cm_view_temple_pgm, name='cm_view_temple_pgm'),
    path('cm_view_winners', views.cm_view_winners, name='cm_view_winners'),
    path('cm_view_video',views.cm_view_video,name='cm_view_video'),
    path('cm_edit_cm_pgm/<int:id>',views.cm_edit_cm_pgm,name='cm_edit_cm_pgm'),
    path('cm_view_winners1', views.cm_view_winners1, name='cm_view_winners1'),

    #member
    path('mbr_chitti_details', views.mbr_chitti_details, name='mbr_chitti_details'),
    path('mbr_chitti_details1', views.mbr_chitti_details1, name='mbr_chitti_details1'),
    path('mbr_edit_profile', views.mbr_edit_profile, name='mbr_edit_profile'),
    path('member_home', views.member_home, name='member_home'),
    path('mbr_payment/<int:id>', views.mbr_payment, name='mbr_payment'),
    path('mbr_profile', views.mbr_profile, name='mbr_profile'),
    path('mbr_registration', views.mbr_registration, name='mbr_registration'),
    path('mbr_view_cm_pgm', views.mbr_view_cm_pgm, name='mbr_view_cm_pgm'),
    path('mbr_view_payment', views.mbr_view_payment, name='mbr_view_payment'),
    path('mbr_view_tmp_pgm', views.mbr_view_tmp_pgm, name='mbr_view_tmp_pgm'),
    path('mbr_view_video', views.mbr_view_video, name='mbr_view_video'),
    path('mbr_view_winner', views.mbr_view_winner, name='mbr_view_winner'),
    path('mbr_view_paid_chitti_status/<int:id>',views.mbr_view_paid_chitti_status,name='mbr_view_paid_chitti_status'),
    path('mbr_pay_month',views.mbr_pay_month,name='mbr_pay_month'),

    #user
    path('usr_adv_payment', views.usr_adv_payment, name='usr_adv_payment'),
    path('usr_aud_booking', views.usr_aud_booking, name='usr_aud_booking'),
    path('usr_declaration/<int:id>', views.usr_declaration, name='usr_declaration'),
    path('usr_edit_profile', views.usr_edit_profile, name='usr_edit_profile'),
    path('user_home', views.user_home, name='user_home'),
    # path('usr_home', views.usr_home, name='usr_home'),
    path('usr_registration', views.usr_registration, name='usr_registration'),
    path('usr_view_adv_payment', views.usr_view_adv_payment, name='usr_view_adv_payment'),
    path('usr_view_aud', views.usr_view_aud, name='usr_view_aud'),
    path('usr_view_aud_bill', views.usr_view_aud_bill, name='usr_view_aud_bill'),
    path('usr_view_booking_sts', views.usr_view_booking_sts, name='usr_view_booking_sts'),
    path('usr_view_tmp_pgm', views.usr_view_tmp_pgm, name='usr_view_tmp_pgm'),
    path('usr_view_video', views.usr_view_video, name='usr_view_video'),
    path('usr_profile',views.usr_profile,name='usr_profile'),
    path('user_terms_and_conditions',views.user_terms_and_conditions,name='user_terms_and_conditions'),

    path('usr_view_history',views.usr_view_history,name='usr_view_history'),



    path('make_pay', views.make_pay, name='make_pay'),
    path('make_payy', views.make_payy, name='make_payy'),
    path('logout', views.logout, name='logout'),

    #def
    path('login2', views.login2, name='login2'),
    path('member_login', views.member_login, name='member_login'),
    path('user_login',views.user_login,name='user_login'),
    path('add_committee',views.add_committee,name='add_committee'),
    path('add_auditorium',views.add_auditorium,name='add_auditorium'),
    path('add_temple_pgm',views.add_temple_pgm,name='add_temple_pgm'),
    path('add_video2',views.add_video2,name='add_video2'),
    path('add_about_chitti1',views.add_about_chitti1,name='add_about_chitti1'),
    path('add_committee_pgm',views.add_committee_pgm,name='add_committee_pgm'),

    path('edit_button_usr_profile',views.edit_button_usr_profile,name='edit_button_usr_profile'),
    path('join_chitti_mbr/<int:id>',views.join_chitti_mbr,name='join_chitti_mbr'),


    #edit(admin)

    path('editmngaud/<int:id>', views.editmngaud, name='editmngaud'),
    path('editmngcm/<int:id>',views.editmngcm,name='editmngcm'),
    path('edittemplepgm/<int:id>',views.edittemplepgm,name='edittemplepgm'),
    path('editvideos/<int:id>',views.editvideos,name='editvideos'),
    path('editaboutchitti/<int:id>',views.editaboutchitti,name='editaboutchitti'),


    path('editcommitteepgm/<int:id>',views.editcommitteepgm,name='editcommitteepgm'),



    #admin -- page def

    path('edit_manage_committee/<int:id>', views.edit_manage_committee, name='edit_manage_committee'),
    path('edit_manage_auditorium/<int:id>',views.edit_manage_auditorium,name='edit_manage_auditorium'),
    path('edit_temple_pgm/<int:id>',views.edit_temple_pgm,name='edit_temple_pgm'),
    path('edit_videos/<int:id>', views.edit_videos, name='edit_videos'),
    path('cm_edit_add_chitti/<int:id>', views.cm_edit_add_chitti, name='cm_edit_add_chitti'),

    #update(admin)

    path('update_committee_mng',views.update_committee_mng,name='update_committee_mng'),
    path('update_manage_auditorium',views.update_manage_auditorium,name='update_manage_auditorium'),
    path('update_temple_pgm',views.update_temple_pgm,name='update_temple_pgm'),
    path('update_videos',views.update_videos,name='update_videos'),



    path('update_committee_pgm',views.update_committee_pgm,name='update_committee_pgm'),

    #update(user)

    path('update_user_profile',views.update_user_profile,name='update_user_profile'),

    #update (meember)

     path('update_member_profile',views.update_member_profile,name='update_member_profile'),

    #update (committee)

    path('update_about_chitti',views.update_about_chitti,name='update_about_chitti'),


    #delete(admin)

    path('delete_videos/<int:id>',views.delete_videos,name='delete_videos'),
    path('delete_temple_pgm/<int:id>',views.delete_temple_pgm,name='delete_temple_pgm'),
    path('delete_manage_auditorium/<int:id>',views.delete_manage_auditorium,name='delete_manage_auditorium'),
    path('delete_manage_committee/<int:id>',views.delete_manage_committee,name='delete_manage_committee'),

    #delete(committee)

    path('delete_about_chitti/<int:id>',views.delete_about_chitti,name='delete_about_chitti'),
    path('delete_cm_pgm/<int:id>',views.delete_cm_pgm,name='delete_cm_pgm'),


    #approve or reject(admin)

    path('approve_user/<int:id>',views.approve_user,name='approve_user'),
    path('reject_user/<int:id>',views.reject_user,name='reject_user'),

    path('approve_user_booking/<int:id>',views.approve_user_booking,name='approve_user_booking'),
    path('reject_user_booking/<int:id>',views.reject_user_booking,name='reject_user_booking'),

    #approve or reject(mcommittee)

    path('approve_member/<int:id>',views.approve_member,name='approve_member'),
    path('reject_member/<int:id>',views.reject_member,name='reject_member'),

    #user button
    path('user_book_button',views.user_book_button,name='user_book_button'),
    path('user_adv_pay',views.user_adv_pay,name='user_adv_pay'),

#search
    #committee
    path('winners_slt_chitti_search',views.winners_slt_chitti_search,name='winners_slt_chitti_search'),
    path('view_winners_slt_chitti_search',views.view_winners_slt_chitti_search,name='view_winners_slt_chitti_search'),
    #member
    path('mbr_view_winners_slt_chitti_search',views.mbr_view_winners_slt_chitti_search,name='mbr_view_winners_slt_chitti_search'),
    path('mbr_join_chitti',views.mbr_join_chitti,name='mbr_join_chitti'),
    path('mbr_join_chitti_search',views.mbr_join_chitti_search,name='mbr_join_chitti_search'),
    path('close_chitti/<int:id>',views.close_chitti,name='close_chitti'),





]