
ENVIROMENT_DEBUG = "http://localhost:9090"
ENVIROMENT_DEBUG_JSON = "http://localhost:8000"
ENVIROMENT_PRODUCTION_JSON = "http://ferremalu.pythonanywhere.com"
ENVIROMENT_PRODUCTION = "https://apiferre.pythonanywhere.com"

ENVIROMENT_JSON_SERVER_DEBUG = './static/'
ENVIROMENT_JSON_SERVER_PRODUCTION = '/home/ferremalu/ferremalu/static/'

ENVIROMENT_FOLDER_LOG_DEBUG = './static/log/'
ENVIROMENT_FOLDER_LOG_PRODUCTION = '/home/ferremalu/ferremalu/static/log/'

#CHANGES CONSTANTS
ENVIROMENT = ENVIROMENT_PRODUCTION
ENVIROMENT_JSON = ENVIROMENT_PRODUCTION_JSON
ENVIROMENT_SERVER_JSON = ENVIROMENT_JSON_SERVER_PRODUCTION
ENVIROMENT_FOLDER_LOG = ENVIROMENT_FOLDER_LOG_PRODUCTION

#CLOSE BOX
CLOSE_BOX_TOTAL = ENVIROMENT + '/close_box/Close_Box_Total/'
GET_LIST_CLOSE_BOX = ENVIROMENT + '/close_box/Get_List_Close_Box/'


GET_INVOICE_CREDIT = ENVIROMENT + '/pos/Get_Invoice_Credit/'

# SETTINGS
TYPE_DOCUMENTI = ENVIROMENT+"/settings/Type_DocumentI/"
TYPE_ORGANIZATIONS = ENVIROMENT+"/settings/Type_Organizations/"
TYPE_REGIMEN = ENVIROMENT+"/settings/Type_Regimen/"
MUNICIPALITYS = ENVIROMENT+"/settings/Municipalitys/"
DISCOUNT_DOCUMENT = "/settings/Discount_Document/"

# EMPLOYEE
VALIDATE_LOGIN = ENVIROMENT+"/employee/Validate_Login/"
GET_LIST_EMPLOYEE = ENVIROMENT+"/employee/GET_LIST_EMPLOYEE/"
GET_EMPLOYEE = ENVIROMENT+"/employee/GET_EMPLOYEE/"
EDIT_EMPLOYEE = ENVIROMENT+"/employee/EDIT_EMPLOYEE/"
REGISTER_EMPLOYEE = ENVIROMENT+"/employee/Register_Employee/"

# CLIENT
GET_LIST_CLIENT = ENVIROMENT+"/client/GET_LIST_CLIENT/"
GET_CLIENT = ENVIROMENT+"/client/GET_CLIENT/"
DELETE_CLIENT = ENVIROMENT+"/client/DELETE_CLIENT/"
CREATE_CLIENT = ENVIROMENT+"/client/CREATE_CLIENT/"
EDIT_CLIENT = ENVIROMENT+"/client/EDIT_CLIENT/"

# INVOICE
CREATE_INVOICE = ENVIROMENT+"/invoice_fe/CREATE_INVOICE/"
GET_LIST_INVOICE = ENVIROMENT+"/invoice_fe/GET_LIST_INVOICE/"
SEND_DIAN = ENVIROMENT+"/invoice_fe/Send_DIAN/"
GET_CONSECUTIVE = ENVIROMENT+"/invoice_fe/GET_CONSECUTIVE/"
GET_INVOICE = ENVIROMENT+"/invoice_fe/GET_INVOICE/"
CREDITNOTE = ENVIROMENT+"/invoice_fe/CreditNote/"
GET_LIST_NOTE_CREDIT = ENVIROMENT+"/invoice_fe/Get_List_Note_Credit/"

# INVENTORY
GET_LIST_INVENTORY = ENVIROMENT+"/inventory/GET_LIST_INVENTORY/"
GET_PRODUCT = ENVIROMENT+"/inventory/GET_PRODUCT/"
UPDATED_PRODUCT = ENVIROMENT+"/inventory/UPDATE_PRODUCT/"
DELETE_PRODUCT = ENVIROMENT+"/inventory/DELETE_PRODUCT/"
CREATE_INVENTORY = ENVIROMENT+"/inventory/CREATE_INVENTORY/"

# SHOPPING
CREATE_SHOPPINGS = ENVIROMENT +"/shopping/CREATE_SHOPPINGS/"
CHECK_INVOICE_NUMBER = ENVIROMENT +"/shopping/CHECK_INVOICE_NUMBER/"





# JSON
FILE_JSON_INVOICE_FE = ENVIROMENT_SERVER_JSON + "data_fe.json"
FILE_JSON_INVOICE_POS = ENVIROMENT_SERVER_JSON + "data_pos.json"
FILE_JSON_EARRING = ENVIROMENT_SERVER_JSON + "earring.json"
FILE_JSON_CLIENTS = ENVIROMENT_SERVER_JSON + "clients.json"
FILE_JSON_INVENTORY = ENVIROMENT_SERVER_JSON + "inventory.json"
FILE_JSON_TYPE_DOCUMENTI = ENVIROMENT_SERVER_JSON + "type_documentI.json"
LIST_EMPLOYEE = ENVIROMENT_SERVER_JSON + "employee.json"

URL_PDF_PLATFORM = 'C:/laragon/www/apidian2021/storage/app/public/'