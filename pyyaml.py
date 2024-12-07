import modal 
app=modal.App(name="test")
image = modal.Image.debian_slim(python_version="3.12").pip_install("pyyaml")
@app.function(image=image)
def run(data1:str):
    import yaml
    with open('boltz.yaml','w') as inp:
        inp.write(data1)
    with open('boltz.yaml','r') as file:
        data=yaml.safe_load(file)
        print(data)
@app.local_entrypoint()
def main():
    yaml_content = """ name: John Doe age: 30 occupation: Developer """
    with open('exp.yaml','w') as file2:
        file2.write(yaml_content)
    with open('exp.yaml','r') as file1:
        data1=str(file)
    run.remote(data1)