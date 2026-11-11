#project 
from pyscript import display, document

def show_sw(e):
    document.getElementById("output").innerHTML = """
    <h3>Seatwork 1</h3>
    <p>Club Member Checker</p>
    <a href="../SW1/sw.html">Open Project</a>
    """

def show_skills(e):
    document.getElementById("output").innerHTML = """
    <h3>Skills Test</h3>
    <p>Periodic Table Element Checker</p>
    <a href="../SKILLSTEST/skills.html">Open Project</a>
    """

def show_drill(e):
    document.getElementById("output").innerHTML = """
    <h3>Drill 2</h3>
    <p>School Club Members</p>
    <a href="../DRILL2/drill.html">Open Project</a>
    """