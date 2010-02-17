def base_template( request ):
    """This sticks the base_template variable defined in the settings
       into the request context, so that we don't have to do it in 
       our render_to_response override."""
    from rapidsms.webui import settings
    
    return {"base_template" : settings.BASE_TEMPLATE}
    





