# -*- coding: utf-8 -*-
"""Task06.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TK5qD88V-RdeLsR6gqQYPCwT01ozMpXJ

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

# TO DO
g.add((ns.University, RDF.type, RDFS.Class))

# Visualize the results
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.2: Add "Researcher" as a subclass of "Person"**"""

# TO DO
g.add((ns.Researcher, RDFS.subClassOf, ns.Person))

# Visualize the results
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.3: Create a new individual of Researcher named "Jane Smithers"**"""

# TO DO
jane = ns.JaneSmithers
g.add((jane, RDF.type, ns.Researcher))
g.add((jane, RDFS.label, Literal("Jane Smithers")))

# Visualize the results
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.4: Add to the individual JaneSmithers the email address, fullName, given and family names. Use the https://schema.org vocabulary**"""

# TO DO
schema = Namespace("https://schema.org/")

g.add((jane, schema.email, Literal("j.smithers@example.com")))
g.add((jane, schema.name, Literal("Jane Smithers")))
g.add((jane, schema.givenName, Literal("Jane")))
g.add((jane, schema.familyName, Literal("Smithers")))

# Visualize the results
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.5: Add UPM as the university where John Smith works. Use the "https://example.org/ namespace**"""

# TO DO
ex_ns = Namespace("https://example.org/")

upm = ex_ns.UPM

g.add((upm, RDF.type, ns.University))

john = ns.JohnSmith
g.add((john, RDFS.label, Literal("John Smith")))
g.add((john, schema.worksFor, upm))

# Visualize the results
for s, p, o in g:
  print(s,p,o)

"""**Task 6.6: Add that Jown knows Jane using the FOAF vocabulary. Make sure the relationship exists.**"""

# TO DO
from rdflib import FOAF

g.add((john, FOAF.knows, jane))

# Visualize the results
for s, p, o in g.triples((None, FOAF.knows, jane)):
  individual = g.value(subject = s, predicate = RDFS.label)
  print(individual)

for s, p, o in g:
  print(s,p,o)