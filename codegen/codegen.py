from optparse import OptionParser
import openai
from dotenv import dotenv_values

def get_completion(prompt, config):
    response = openai.Completion.create(
        # model="code-davinci-002",
        model=config['model'],
        prompt=prompt,
        temperature=config['temperature'],
        max_tokens=config['max_tokens'],
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-p', '--prompt', dest='prompt',
        help='The path to file containing the prompt text')
    parser.add_option('-m', '--model', dest='model', default='code-davinci-002',
        help='''The model to use. Options:
1.  text-davinci-003
2.  text-curie-001
3.  text-babbage-001
4.  text-ada-001
5.  text-davinci-002
6.  text-davinci-001
7.  davinci-instruct-beta
8.  davinci
9.  curie-instruct-beta
10. curie
11. babbage
12. ada
13. code-davinci-002
14. code-cushman-001''')
    parser.add_option('-o', '--output', dest='output', default='a.out',
        help='The output file to store the result')
    parser.add_option('-t', '--temperature', dest='temperature', default=0,
        help='The temperature of the model')
    parser.add_option('-l', '--maxlength', dest='maxlength', default=256,
        help='The maximum number of tokens in the response')
    parser.add_option('-k', '--keyfile', dest='keyfile', default='.env',
        help='The file that holds the api key for openai')

    (options, args) = parser.parse_args()

    config = dotenv_values(options.keyfile)
    openai.api_key = config['OPENAI_API_KEY']

    with open(options.prompt, 'r') as input_file:
        prompt = input_file.read()
    
    config = {
        'model': options.model,
        'temperature': float(options.temperature),
        'max_tokens': int(options.maxlength)
    }

    resp = get_completion(prompt, config)

    with open(options.output, 'w') as file:
        file.write(prompt)
        file.write(resp.choices[0].text)
