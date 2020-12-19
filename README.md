# HL7 FHIR Manifold
HL7 FHIR Manifold is a script that manifolds the last elements of a different types of information that can be found in a HL7 FHIR server, it sorts by appereances and it represents graphically in a Excel file.

## Manifoldable information types
This project manifold the following types of information:
- [Diagnostic Reports](http://hl7.org/fhir/R4/diagnosticreport.html)
- [Observations](http://hl7.org/fhir/R4/observation.html)
- [Medications](http://hl7.org/fhir/R4/medication.html)

## Dependences
To use it, you need to install [XlsxWriter](https://github.com/jmcnamara/XlsxWriter)

```sh
$ pip3 install XslxWriter
```

## Usage
```sh
$ python3 client.py
Type the number of elements to manifold: XXX
Manifolding...
Done!
```
Where *XXX* is the number of last elements to manifold.

## References
- http://hapi.fhir.org/
- https://hapifhir.io/