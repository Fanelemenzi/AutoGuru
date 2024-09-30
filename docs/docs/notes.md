System requirements
- virtual environment
- pip install  django
- pip install pillow to handle images

# Changes Tracker based on dates
### 29 Sept
Development notes/issues: models design and code
- change max_length for vehicle_ID in VIN model
- add vin on other models

- chnage max_lenght for Inspection number
- change max length for Inspection results and check for dropdown field option
- dropdown option added
    1. Passed
    2. Passed with minor defects
    3. Passed with major defects
    4. Failed due minor defects
    5. Failed due major defects
    5. Failed
- change max length for link ot results

- change max length on work perfomed

### 30 Sept
- django code on models for multiple images uploads
- add the vin details like in the GPT search results where vin model is linked to other models. you can even separate the vin model to a sole model and add it on each other models