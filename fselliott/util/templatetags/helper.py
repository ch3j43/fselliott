from django import template
from django.utils.safestring import mark_safe
from django.utils.translation import string_concat

register = template.Library()

@register.filter
def form_field(value):
    try:
        err = ""
        err_cls = ""
        if value.errors:
            err_cls = "error"
            for e in value.errors:
                err ="""
                    <span class="help-inline">%s</span>
                """ % e    
        
        field = """
            <div class="control-group %s">
                <label class="control-label" for="id_%s">%s:</label>
                <div class="controls">
                    %s
                    %s
                </div>
            </div>
        """ % (err_cls, unicode(value.name), unicode(value.label), value, err)
        
        return mark_safe(field)
    except:
        return value
