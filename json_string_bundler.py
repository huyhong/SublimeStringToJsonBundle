import sublime, sublime_plugin
import re, string

def to_upper_snake_case(text):
    text = re.sub('[-. _]+', '_', text).lower()
    return re.sub('(?<=[^_])([A-Z])', r'_\1', text).upper()

def remove_punctuation(text):
    exclude = set(string.punctuation)
    text = ''.join(ch for ch in text if ch not in exclude)
    return text

def to_underscore(text):
    return text.replace(" ", "_")

def to_dot_case(text):
    return text.replace("_", ".")

def to_dash_case(text):
    return text.replace("_", "-")

def to_slash(text):
    return text.replace("_", "/")

def to_separate_words(text):
    return text.replace("_", " ")

def escape_double_quotes(text): 
    return text.replace('"','\\"')

def to_json_bundle(text):
    escaped_text = escape_double_quotes(text)
    text_array = remove_punctuation(escaped_text).split(' ', 7)
    if(len(text_array) >= 7):
        text_array.pop()
    json_text = " ".join(text_array)
    json_text = to_upper_snake_case(json_text)
    return "\"" + json_text + "\":" + " \"" + escaped_text + "\","

def run_on_selections(view, edit, func):
    for s in view.sel():
        region = view.line(s)
        text = view.substr(region)
        view.replace(edit, region, func(text))

class ConvertToJsonBundleCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        run_on_selections(self.view, edit, to_json_bundle)
