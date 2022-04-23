from fastapi import FastAPI

app = FastAPI()

fruits = []

@app.get('/')
def Home():
    return {"message" : "Hello"}

@app.post('/add_fruits')
def add_fruits(fruit):
    fruits.append(fruit)
    return {"fruit added": fruits[-1]}

@app.get('/fruits')
def get_all():
    return fruits

@app.delete('/delete_fruit/{fruit_index}')
def delete_fruit(fruit_index :int ):
    fruits.pop(fruit_index)
    return fruits