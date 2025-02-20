from cerberus import Validator

def events_creator_validator(request: any): #vai ser o mesmo request do flask
  body_validator = Validator({
      "data": {
         "type": "dict",
         "schema" : {
           "name": {"type": "string", "required": True, "empty": False} #cerberus ajuda a não ter que fazer if/else 
         }
      }
   })
  
  response = body_validator.validate(request.json) #esse body_validator está validando o body do flask

  if response is False:
    raise Exception(body_validator.errors)

