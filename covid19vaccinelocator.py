import matplotlib.pyplot as plt
plt.style.use('classic')

# Note: this script will not run without specifying the input data
# Manually insert file path of text document at the {file_path} with vaccine location list as *.txt document
with open("{file_path}", "r") as f:
	data = f.read()

# Place each cluster of information into separate item in list
dataEnd =  False

# Make a list of all of the vaccine administration locations
vaccineLocations = []

while (dataEnd == False):
    # Find the position where the Updated line is contained
    pos = data.find("Updated")
    # Find the relative position of newline character after the 'Updated' text
    # Add this position to the position of "Updated" to find total position
    new = data[pos:].find("\n")+pos
    # Identify cluster of data up to this newline
    # Append it as an item to the vaccineLocations list
    cluster = data[:new]
    #print(cluster)
    cluster = cluster.lstrip()
    vaccineLocations.append(cluster)
    # Update the dataset to contain everything after the newline character
    data = data[new:]
    if (len(data) < 25):
        dataEnd = True

# Create a database of availability
locationDatabase = {}

x2 = []
y2 = []
x1 = []
y1 = []

# Add each location (the first line in each cluster) to a locationDatabase
for each in vaccineLocations:
    locationDatabase[each[:each.find("\n")]] = []
    
    if "no appointments available" in each.lower():
        locationDatabase[each[:each.find("\n")]].append("No Vaccine Available Currently")
        locationDatabase[each[:each.find("\n")]].append(each[each.find(" mi")-4:each.find(" mi")+1].lstrip().rstrip())
        x2.append(float(each[each.find(" mi")-4:each.find(" mi")+1].lstrip().rstrip()))
        y2.append(float(0))
    else:
        locationDatabase[each[:each.find("\n")]].append("Vaccine Available Currently")
        locationDatabase[each[:each.find("\n")]].append(each[each.find(" mi")-4:each.find(" mi")+1].lstrip().rstrip())
        x1.append(float(each[each.find(" mi")-4:each.find(" mi")+1].lstrip().rstrip()))
        y1.append(float(0))
        
# Create plots of available vaccine

fig, axs = plt.subplots(2)
fig.suptitle("All COVID-19 vaccinations sites within a 50 mile radius,\n[based on availability and distance]")
axs[0].plot(x1, y1, color="#D097D7", marker='o')
axs[1].plot(x2, y2, color="#F4D8F8", marker='o')
#axs[0].get_yaxis().set_visible(False)
axs[0].set_xlabel('Distance (mi.)')
axs[0].set_ylabel('Available')
axs[0].set_yticklabels([])
#axs[1].get_yaxis().set_visible(False)
axs[1].set_xlabel('Distance (mi.)')
axs[1].set_ylabel('Unavailable')
axs[1].set_yticklabels([])
fig.tight_layout(pad=3.0)
plt.show()

# Create subsets for distance ranges
# Walking distance (< 1.5 miles)

walkingDistanceAvailable = []
notWalkingDistanceAvailable = []
walkingDistanceUnavailable = []
notWalkingDistanceUnavailable = []

for each in locationDatabase:
    if (locationDatabase[each][0] == "No Vaccine Available Currently"):
        if (float(locationDatabase[each][1]) < 1.5):
            walkingDistanceUnavailable.append(each)
        else:
            notWalkingDistanceUnavailable.append(each)
    else:
        if (float(locationDatabase[each][1]) < 1.5):
            walkingDistanceAvailable.append(each)
        else:
            notWalkingDistanceAvailable.append(each)

# Note: short walking distance category determined based on 30 minutes of walking
# Note: Approximation of 5 minutes to walk 0.25 miles based on reference from WalkScore
# Reference: https://www.walkscore.com/methodology.shtml
print("# locations with vaccine available within a short walking distance:")
print(len(walkingDistanceAvailable))

print("# locations with vaccine available requiring longer walking distance or other transport:")
print(len(notWalkingDistanceAvailable))

print("# locations with no availability within a short walking distance:")
print(len(walkingDistanceUnavailable))

print("# locations with no availability requiring longer walking distance or other transport:")
print(len(notWalkingDistanceUnavailable))
