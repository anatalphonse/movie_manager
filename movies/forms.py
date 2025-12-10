from django.forms import ModelForm
from django import forms
from . models import MovieInfo

class MovieForm(ModelForm):
    class Meta:
        model = MovieInfo
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'block w-full px-4 py-3 rounded-lg border border-slate-300 bg-slate-50 focus:bg-white focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-colors duration-200 outline-none'}),
            'year': forms.NumberInput(attrs={'class': 'block w-full px-4 py-3 rounded-lg border border-slate-300 bg-slate-50 focus:bg-white focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-colors duration-200 outline-none'}),
            'decsription': forms.Textarea(attrs={'class': 'block w-full px-4 py-3 rounded-lg border border-slate-300 bg-slate-50 focus:bg-white focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-colors duration-200 outline-none', 'rows': 4}),
            'poster': forms.FileInput(attrs={'class': 'block w-full text-sm text-slate-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-indigo-50 file:text-indigo-700 hover:file:bg-indigo-100'}),
            'censor_details': forms.Select(attrs={'class': 'block w-full px-4 py-3 rounded-lg border border-slate-300 bg-slate-50 focus:bg-white focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-colors duration-200 outline-none'}),
            'director_by': forms.Select(attrs={'class': 'block w-full px-4 py-3 rounded-lg border border-slate-300 bg-slate-50 focus:bg-white focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-colors duration-200 outline-none'}),
            'acters': forms.SelectMultiple(attrs={'class': 'block w-full px-4 py-3 rounded-lg border border-slate-300 bg-slate-50 focus:bg-white focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-colors duration-200 outline-none'}),
        }