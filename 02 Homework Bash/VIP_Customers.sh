#Creates a folder called AllRecords
mkdir AllRecords

#finds and copies all of the order records from 2012-2017 in the the All Records Folder
find . -type f -iname *.csv* -exec cp {} AllRecords/ \;

#Creates and folder call VIPCUstomersOrders inside of AllRecords
mkdir AllRecords/VIPCustomerOrders

#Finds all order for Michael Campbell and places them in a file called michael_campbell_orders.output
grep -r "Michael,Campbell" AllRecords/ >> AllRecords/VIPCustomerOrders/michael_campbell_orders.output

#Finds all order for Michael Davis and places them in a file called michael_davis_orders.output
grep -r "Michael,Davis" AllRecords/ >> AllRecords/VIPCustomerOrders/michael_davis_orders.output

#counts the orders for Michael Campbell
grep -r "Michael,Campbell" AllRecords/VIPCustomerOrders/ | wc -l >> VIPCustomerDetails.md

#counts the orders for Michael Davis
grep -r "Michael,Davis" AllRecords/VIPCustomerOrders/ | wc -l >> VIPCustomerDetails.md