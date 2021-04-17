# covid19vaccinelocator

## Description:
The covid19vaccinelocator is intended to compile data for proximal vaccine clinic and illustrate distance charts based on whether vaccine is `available` or `unavailable`

## User requirement
User input is required as manual entry at the `# Insert file path of text document with trimmed location list` section of code.


# Input data format
Please consider the following when trimming data set, as each entry needs to adhere to the following format:
- Name of vaccine clinic
- Location of vaccine clinic
- Newline
- "[Float #] mi." (No more than 3 digits including 1 decimal point of precision, example: "37.8 mi" or "1.4 mi")
- Newline
- Type of service
- Vendor of vaccine
- Newline
- "Appointments available" or "No Appointments available"
- Newline
- "Updated {time duration} ago"

All entries can be concatenated together in one singular .txt file

## Reference
Please refer to [Washington State Department of Health Website](https://vaccinelocator.doh.wa.gov/) in order to source raw data.
If user lives in a different state, formatting may be different and may require modification of the python script.

## Special note
A special note of thanks to *Washington State Department of Health* for creating a useful web aggregation tool.

## Additional special note
An extra special note to all facility workers, governement employees, healthcare providers, doctors, nurses, administrators, and countless others...
### One Nation...

