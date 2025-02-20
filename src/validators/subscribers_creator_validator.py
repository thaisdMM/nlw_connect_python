from cerberus import Validator

def subscribers_creator_validator(request: any): #vai ser o mesmo request do flask

#cerberus ajuda a construir validadores sem ter que fazer if/else 
  body_validator = Validator({
      "data": {
         "type": "dict",
         "schema" : {
           "name": {"type": "string", "required": True, "empty": False}, 
           "email": {"type": "string", "required": True, "empty": False},
           "link": {"type": "string",  "required": False, "empty": False},
            "evento_id": {"type": "integer",  "required": True, "empty": False},
      
      }
      }
      })
  
  response = body_validator.validate(request.json) #esse body_validator está validando o body do flask

  if response is False:
    raise Exception(body_validator.errors)
