from django.shortcuts import redirect, render

def test(request):
	return render(request, "zenix/testing/demo.html")

def test2(request,pk):
	return render(request, "zenix/testing/demo.html")

#*******************************************************************************
def index(request):
	return render(request, "zenix/index.html")

def index_2(request):
	return render(request, "zenix/index-2.html")


def my_wallets(request):
	
	return render(request, "zenix/my-wallets.html")

def tranasactions(request):
	return render(request, "zenix/tranasactions.html")

def coin_details(request):
	return render(request, "zenix/coin-details.html")

def portofolio(request):
	return render(request, "zenix/portofolio.html")

def market_capital(request):
	return render(request, "zenix/market-capital.html")

#Apps

def app_profile(request):
	return render(request, "zenix/apps/app-profile.html")
	
def post_details(request):
	return render(request, "zenix/apps/post-details.html")

def page_chat(request):
	return render(request, "zenix/apps/page-chat.html")

def project_list(request):
	return render(request, "zenix/apps/project/project-list.html")


def project_card(request):
	return render(request, "zenix/apps/project/project-card.html")

def user_list_datatable(request):

	return render(request, "zenix/apps/user/user-list-datatable.html")

def user_list_column(request):
	return render(request, "zenix/apps/user/user-list-column.html")

def contact_list(request):
	return render(request, "zenix/apps/contact/contact-list.html")

def contact_card(request):
	return render(request, "zenix/apps/contact/contact-card.html")

#email
def email_compose(request):
	return render(request, "zenix/apps/email/email-compose.html")

def email_inbox(request):
	return render(request, "zenix/apps/email/email-inbox.html")

def email_read(request):
	return render(request, "zenix/apps/email/email-read.html")

def app_calender(request):
	return render(request, "zenix/apps/app-calender.html")

#shop

def ecom_checkout(request):
	return render(request, "zenix/apps/shop/ecom-checkout.html")
def ecom_customers(request):
	return render(request, "zenix/apps/shop/ecom-customers.html")
def ecom_invoice(request):
	return render(request, "zenix/apps/shop/ecom-invoice.html")
def ecom_product_detail(request):
	return render(request, "zenix/apps/shop/ecom-product-detail.html")
def ecom_product_grid(request):
	return render(request, "zenix/apps/shop/ecom-product-grid.html")
def ecom_product_list(request):
	return render(request, "zenix/apps/shop/ecom-product-list.html")
def ecom_product_order(request):
	return render(request, "zenix/apps/shop/ecom-product-order.html")

#charts

def chart_chartist(request):
	return render(request, "zenix/charts/chart-chartist.html")
def chart_chartjs(request):
	return render(request, "zenix/charts/chart-chartjs.html")
def chart_flot(request):
	return render(request, "zenix/charts/chart-flot.html")
def chart_morris(request):
	return render(request, "zenix/charts/chart-morris.html")
def chart_peity(request):
	return render(request, "zenix/charts/chart-peity.html")
def chart_sparkline(request):
	return render(request, "zenix/charts/chart-sparkline.html")

#Components
#---->Bootstrap

def ui_accordion(request):
	return render(request, "zenix/components/bootstrap/ui-accordion.html")

def ui_alert(request):
	return render(request, "zenix/components/bootstrap/ui-alert.html")

def ui_badge(request):
	return render(request, "zenix/components/bootstrap/ui-badge.html")

def ui_button(request):
	return render(request, "zenix/components/bootstrap/ui-button.html")

def ui_modal(request):
	return render(request, "zenix/components/bootstrap/ui-modal.html")

def ui_button_group(request):
	return render(request, "zenix/components/bootstrap/ui-button-group.html")

def ui_list_group(request):
	return render(request, "zenix/components/bootstrap/ui-list-group.html")

def ui_media_object(request):
	return render(request, "zenix/components/bootstrap/ui-media-object.html")

def ui_card(request):
	return render(request, "zenix/components/bootstrap/ui-card.html")

def ui_carousel(request):
	return render(request, "zenix/components/bootstrap/ui-carousel.html")

def ui_dropdown(request):
	return render(request, "zenix/components/bootstrap/ui-dropdown.html")

def ui_popover(request):
	return render(request, "zenix/components/bootstrap/ui-popover.html")

def ui_progressbar(request):
	return render(request, "zenix/components/bootstrap/ui-progressbar.html")

def ui_tab(request):
	return render(request, "zenix/components/bootstrap/ui-tab.html")

def ui_typography(request):
	return render(request, "zenix/components/bootstrap/ui-typography.html")

def ui_pagination(request):
	return render(request, "zenix/components/bootstrap/ui-pagination.html")

def ui_grid(request):
	return render(request, "zenix/components/bootstrap/ui-grid.html")

#Plugins

def uc_select2(request):
	return render(request, "zenix/components/plugins/uc-select2.html")
def uc_nestable(request):
	return render(request, "zenix/components/plugins/uc-nestable.html")

def uc_noui_slider(request):
	return render(request, "zenix/components/plugins/uc-noui-slider.html")

def uc_sweetalert(request):
	return render(request, "zenix/components/plugins/uc-sweetalert.html")

def uc_toastr(request):
	return render(request, "zenix/components/plugins/uc-toastr.html")

def map_jqvmap(request):
	return render(request, "zenix/components/plugins/map-jqvmap.html")

def uc_lightgallery(request):
	return render(request, "zenix/components/plugins/uc-lightgallery.html")


# Widget Basic

def widget_basic(request):
	return render(request, "zenix/components/widget-basic.html")


#Forms


def form_element(request):
	return render(request, "zenix/components/forms/form-element.html")

def form_wizard(request):
	return render(request, "zenix/components/forms/form-wizard.html")

def form_editor_summernote(request):
	return render(request, "zenix/components/forms/form-editor-summernote.html")

def form_pickers(request):
	return render(request, "zenix/components/forms/form-pickers.html")

def form_validation_jquery(request):
	return render(request, "zenix/components/forms/form-validation-jquery.html")

#Table
def table_bootstrap_basic(request):
	return render(request, "zenix/components/table/table-bootstrap-basic.html")


def table_datatable_basic(request):
	return render(request, "zenix/components/table/table-datatable-basic.html")

#pages

def page_register(request):
	return render(request, "zenix/components/pages/page-register.html")

def page_login(request):
	return render(request, "zenix/components/pages/page-login.html")

def page_error_400(request):
	return render(request, "400.html")

def page_error_403(request):
	return render(request, "403.html")

def page_error_404(request):
	return render(request, "404.html")

def page_error_500(request):
	return render(request, "500.html")

def page_error_503(request):
	return render(request, "503.html")

def page_lock_screen(request):
	return render(request, "zenix/components/pages/page-lock-screen.html")



def page_forgot_password(request):
	return render(request, "zenix/components/pages/page-forgot-password.html")






