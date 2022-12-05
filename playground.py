
import re
content = '''
py to ts

```
def predict_proba(X: Iterable[str]):
  return np.array([predict_one_probas(tweet) for tweet in X])
```
'''

regex = r"([a-z]{2}) to ([a-z]{2})" 
match = re.search(regex, content)

start_lang = match.group(1)
end_lang = match.group(2)

code_regex = r"```((.|\n)*)```"
match = re.search(code_regex, content)
start_code = match.group(1)


prompt = ''
prompt += f'##### Translate this function from {start_lang} into {end_lang}\n'
prompt += f'### {start_lang}\n'
prompt += start_code
prompt += '\n'
prompt += f'### {end_lang}\n'
prompt += '\n'

print(prompt)
