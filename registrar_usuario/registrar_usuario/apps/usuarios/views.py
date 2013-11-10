from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from forms import *

def usuarios(request, template= 'usuarios/usuarios.html'):
	usuarios = User.objects.all()
	c = {'usuarios':usuarios}
	return render_to_response(template, c, context_instance=RequestContext(request))

def registrar(request):
	template = 'usuarios/registrar.html'

	if request.method=='POST':
		formulario = RegistrationForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect( '/' )
	else:
		formulario = RegistrationForm()
		
	return render_to_response(template,{'formulario':formulario}, context_instance=RequestContext(request))
