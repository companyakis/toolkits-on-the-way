from flask import Flask

app = Flask(__name__)

departments = [
    {
        "dep_name": "Sales",
        "dep_info": [
            {
                "dep_head": "Ayhan Bilir",
                "number_of_dep_emps": 17
            }
        ]
    },
    
    {
        "dep_name": "HR",
        "dep_info": [
            {
                "dep_head": "Bilge Yolcu",
                "number_of_dep_emps": 3
            }
        ]
    }
]

@app.get("/departments")
def get_deps_info():
    
    return {"departments": departments}


if __name__ == "__main__":
    app.run(debug=True)
