# CuntWeb
## Layout
* [Model](#Model)
* [View](#View)
* [Heroku](#Heroku)

## Model
![Image of model](/cuntweb_pics/model.JPG)
![Image of model](/cuntweb_pics/web_01.JPG)
![Image of model](/cuntweb_pics/web_02.JPG)
	
## View
Context_status:

Setting the status for checking action of user

context{
'plate_search': 'successful',
'search_status': 'parts',
'plate': platematch,
'main_data': typematch.type_model.all(),
'history': history_list[1],
'hischeck': history_list[0],
}

* plate_search: have been searched or not
* search_status: depend on the status to show the home page or others
* plate: which platenumber is active and get the data from this plate
* main_data: the path of data what user need
* history & hischeck: the fix history data
* otehrs: the special situation
	
## Heroku

