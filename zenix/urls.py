from django.urls import path, include
from zenix import zenixViews

urlpatterns = [

	path('',zenixViews.index,name="index"),
	path('index/',zenixViews.index,name="index"),
	path('index_2/',zenixViews.index_2,name="index-2"),
	path('my_wallets/',zenixViews.my_wallets,name="my-wallets"),
	path('tranasactions/',zenixViews.tranasactions,name="tranasactions"),
	path('coin_details/',zenixViews.coin_details,name="coin-details"),
	path('portofolio/',zenixViews.portofolio,name="portofolio"),
	path('market_capital/',zenixViews.market_capital,name="market-capital"),
	#Apps
	path('app_profile/',zenixViews.app_profile,name="app-profile"),
	path('post_details/',zenixViews.post_details,name="post-details"),
	#Chat
	path('page_chat/',zenixViews.page_chat,name="page-chat"),
	#project
	path('project_list/',zenixViews.project_list,name="project-list"),
	path('project_card/',zenixViews.project_card,name="project-card"),
	#user
	path('user_list_datatable/',zenixViews.user_list_datatable,name="user-list-datatable"),
	path('user_list_column/',zenixViews.user_list_column,name="user-list-column"),
	#contact
	path('contact-list/',zenixViews.contact_list,name="contact-list"),
	path('contact-card/',zenixViews.contact_card,name="contact-card"),
	#email
	path('email_compose/',zenixViews.email_compose,name="email-compose"),
	path('email_inbox/',zenixViews.email_inbox,name="email-inbox"),
	path('email_read/',zenixViews.email_read,name="email-read"),

	#Calender
	path('app_calender/',zenixViews.app_calender,name="app-calender"),
	
	#shop
	path('ecom_checkout/',zenixViews.ecom_checkout,name="ecom-checkout"),
	path('ecom_customers/',zenixViews.ecom_customers,name="ecom-customers"),
	path('ecom_invoice/',zenixViews.ecom_invoice,name="ecom-invoice"),
	path('ecom_product_detail/',zenixViews.ecom_product_detail,name="ecom-product-detail"),
	path('ecom_product_grid/',zenixViews.ecom_product_grid,name="ecom-product-grid"),
	path('ecom_product_list/',zenixViews.ecom_product_list,name="ecom-product-list"),
	path('ecom_product_order/',zenixViews.ecom_product_order,name="ecom-product-order"),
	
	#charts
	path('chart_chartist/',zenixViews.chart_chartist,name="chart-chartist"),
	path('chart_chartjs/',zenixViews.chart_chartjs,name="chart-chartjs"),
	path('chart_flot/',zenixViews.chart_flot,name="chart-flot"),
	path('chart_morris/',zenixViews.chart_morris,name="chart-morris"),
	path('chart_peity/',zenixViews.chart_peity,name="chart-peity"),
	path('chart_sparkline/',zenixViews.chart_sparkline,name="chart-sparkline"),

	#Components
	#---->Bootstrap
	path('ui_accordion/',zenixViews.ui_accordion,name="ui-accordion"),
	path('ui_alert/',zenixViews.ui_alert,name="ui-alert"),
	path('ui_badge/',zenixViews.ui_badge,name="ui-badge"),
	path('ui_button/',zenixViews.ui_button,name="ui-button"),
	path('ui_modal/',zenixViews.ui_modal,name="ui-modal"),
	path('ui_button_group/',zenixViews.ui_button_group,name="ui-button-group"),
	path('ui_list_group/',zenixViews.ui_list_group,name="ui-list-group"),
	path('ui_media_object/',zenixViews.ui_media_object,name="ui-media-object"),
	path('ui_card/',zenixViews.ui_card,name="ui-card"),
	path('ui_carousel/',zenixViews.ui_carousel,name="ui-carousel"),
	path('ui_dropdown/',zenixViews.ui_dropdown,name="ui-dropdown"),
	path('ui_popover/',zenixViews.ui_popover,name="ui-popover"),
	path('ui_progressbar/',zenixViews.ui_progressbar,name="ui-progressbar"),
	path('ui_tab/',zenixViews.ui_tab,name="ui-tab"),
	path('ui_typography/',zenixViews.ui_typography,name="ui-typography"),
	path('ui_pagination/',zenixViews.ui_pagination,name="ui-pagination"),
	path('ui_grid/',zenixViews.ui_grid,name="ui-grid"),

	#Components
	#---->Plugins
	path('uc_select2/',zenixViews.uc_select2,name="uc-select2"),
	path('uc_nestable/',zenixViews.uc_nestable,name="uc-nestable"),
	path('uc_noui_slider/',zenixViews.uc_noui_slider,name="uc-noui-slider"),
	path('uc_sweetalert/',zenixViews.uc_sweetalert,name="uc-sweetalert"),
	path('uc_toastr/',zenixViews.uc_toastr,name="uc-toastr"),
	path('map_jqvmap/',zenixViews.map_jqvmap,name="map-jqvmap"),
	path('uc_lightgallery/',zenixViews.uc_lightgallery,name="uc-lightgallery"),
	#Widget Basic
	path('widget_basic/',zenixViews.widget_basic,name="widget-basic"),
	#forms
	path('form_element/',zenixViews.form_element,name="form-element"),
	path('form_wizard/',zenixViews.form_wizard,name="form-wizard"),
	path('form_editor_summernote/',zenixViews.form_editor_summernote,name="form-editor-summernote"),
	path('form_pickers/',zenixViews.form_pickers,name="form-pickers"),
	path('form_validation_jquery/',zenixViews.form_validation_jquery,name="form-validation-jquery"),

	#table
	path('table_bootstrap_basic/',zenixViews.table_bootstrap_basic,name="table-bootstrap-basic"),
	path('table_datatable_basic/',zenixViews.table_datatable_basic,name="table-datatable-basic"),
	
	#Pages
	path('page_register/',zenixViews.page_register,name="page-register"),
	path('page_login/',zenixViews.page_login,name="page-login"),
	path('page_error_400/',zenixViews.page_error_400,name="page-error-400"),
	path('page_error_403/',zenixViews.page_error_403,name="page-error-403"),
	path('page_error_404/',zenixViews.page_error_404,name="page-error-404"),
	path('page_error_500/',zenixViews.page_error_500,name="page-error-500"),
	path('page_error_503/',zenixViews.page_error_503,name="page-error-503"),
	path('page_lock_screen/',zenixViews.page_lock_screen,name="page-lock-screen"),
	path('page_forgot_password/',zenixViews.page_forgot_password,name="page-forgot-password"),
	



	

	#path('',zenixViews.index,name="index"),
	#testing
	path('test/',zenixViews.test,name="test"),
	path('test2/<int:pk>/',zenixViews.test2,name="test2"),
	

]
