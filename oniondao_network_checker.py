import requests
from datetime import datetime

def main():
        date = datetime.now() # Get the current date and assign it to "date"
        dateprint = str(date) # Convert "date" into a string and assign it to "dateprint"
        dateprint = dateprint[:19] # Truncate "dateprint" to the date and time
        datename = dateprint[:10] # Truncate "dateprint" to just the date
        nodes = 0 # Assign "nodes" to keep track of the amount of OnionDAO nodes

        outfile = open(datename + ".txt", "w") # Create a writeable file named "datename.txt"

        response1 = requests.get("https://oniondao.web.app/api/tor_nodes/list/wallet") # Retrieve the participating wallets from OnionDAO
        wallets = response1.json() # Assigns the response from OnionDAO to "wallets"
        for wallet in wallets: # Creates a loop, writing each wallet on a different line and summing the total OnionDAO nodes
                print(wallet)
                outfile.write(wallet + "\n")
                nodes = nodes + 1
        print("\n" + "Number of OnionDAO Nodes: ", nodes) # Print the number of OnionDAO nodes
        nodes = str(nodes) # Converts the "nodes" value into a string
        outfile.write("\n" + "Number of OnionDAO Nodes: " + nodes + "\n" + "\n") # Write the number of OnionDAO nodes
        print("")

        response2 = requests.get("https://oniondao.web.app/api/tor_nodes/metrics") # Retrieve OnionDAO metrics
        percent = response2.json() # Assigns the response from OnionDAO to "percent"
        percent = str(percent["percent_contribution"]) # Converts the "percent" value into a string
        print("OnionDAO percent of the Tor network: " + percent + "%") # Prints the "percent" value retrieved from OnionDAO
        outfile.write("OnionDAO percent of the Tor network: " + percent + "%" + "\n" + "\n") # Writes the percent to the file
        
        outfile.write(dateprint) # Write the current date and time to the end of the file

        outfile.close()
main()