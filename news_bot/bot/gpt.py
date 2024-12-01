
from openai import OpenAI
import urllib

key="sk-h3Kos89nCFLTOsw9444f1e2657C54eFcB726005f1e448001"
client = OpenAI(
    api_key="sk-h3Kos89nCFLTOsw9444f1e2657C54eFcB726005f1e448001", 
    base_url="https://api.aiguoguo199.com/v1"
)

def generate_one(prompt, path_folder,name):
    response = client.images.generate(
        prompt=f"{prompt}",
        n=1,
        size="1024x1024"
    )
    url = response.data[0].url
    urllib.request.urlretrieve(url,f"{path_folder}/{name}")
    return f"{path_folder}/{name}.png"
    