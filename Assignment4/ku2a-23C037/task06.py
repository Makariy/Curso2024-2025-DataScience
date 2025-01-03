# -*- coding: utf-8 -*-
"""Task06.ipynb
Automatically generated by Colab.
Original file is located at
    https://colab.research.google.com/drive/1UBwVe20COkfVvGiik0iZqDmci72tR4hn
**Task 06: Modifying RDF(s)**
"""

!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2024-2025/master/Assignment4/course_materials"

"""Read the RDF file as shown in class"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example5.rdf", format="xml")

"""Create a new class named Researcher"""

ns = Namespace("http://somewhere#")
g.add((ns.Researcher, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.1: Create a new class named "University"**
"""

g.add((ns.University, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.2: Add "Researcher" as a subclass of "Person"**"""

g.add((ns.Researcher, RDFS.subClassOf, ns.Person ))
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.3: Create a new individual of Researcher named "Jane Smithers"**"""

name = Literal("Jane Smithers")
g.add((ns.JaneSmithers,RDF.type, ns.Researcher))
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.4: Add to the individual JaneSmithers the email address, fullName, given and family names. Use the https://schema.org vocabulary**"""

SCHEMA = Namespace('https://schema.org/')
g.add((ns.JaneSmithers, SCHEMA.email, Literal("janesmitheres@gmail.com")))
g.add((ns.JaneSmithers, SCHEMA.name, Literal("Jane Smithers")))
g.add((ns.JaneSmithers, SCHEMA.givenName, Literal("Jane")))
g.add((ns.JaneSmithers, SCHEMA.familyName, Literal("Smithers")))

"""**TASK 6.5: Add UPM as the university where John Smith works. Use the "https://example.org/ namespace**"""

EX = Namespace("https://example.org/")
g.add((EX.UPM, RDF.type, ns.University))
g.add((ns.JohnSmith,SCHEMA.worksFor, EX.UPM))

"""**Task 6.6: Add that Jown knows Jane using the FOAF vocabulary. Make sure the relationship exists.**"""

from rdflib import FOAF
g.add((ns.JhonSmith, FOAF.knows, ns.JaneSmith))

for s,p,o in g.triples((ns.JhonSmith, FOAF.knows,None)):
  print(o)