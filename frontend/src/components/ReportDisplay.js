import React, {useState, useEffect, useRef, useMemo, useCallback} from 'react'
import { AgGridReact } from 'ag-grid-react';

import 'ag-grid-community/styles/ag-grid.css'; 
import 'ag-grid-community/styles/ag-theme-alpine.css'; 

const AppPage = () => {
   const gridRef = useRef();
   const [rowData, setRowData] = useState();

    // Each Column Definition results in one Column.
 const [columnDefs, setColumnDefs] = useState([
   {field: 'program_time', },
   {field: '_start'},
   {field: '_stop'},
   {field: 'actual_time'},
   {field: '_report'}
 ]);

 // DefaultColDef sets props common to all Columns
 const defaultColDef = useMemo( ()=> ({
     sortable: true
   }));

 // Example of consuming Grid Event
 const cellClickedListener = useCallback( event => {
   console.log('cellClicked', event);
 }, []);
   useEffect(() => {
      fetch('http://127.0.0.1:8000/report/')
         .then((response) => response.json())
         .then((rowData) => {
            setRowData(rowData);
         })
         .catch((err) => {
            console.log(err.message);
         });
   }, []);


 const buttonListener = useCallback( e => {
   gridRef.current.api.deselectAll();
 }, []);
 return (
   <div>

     {/* Example using Grid's API */}
     <button onClick={buttonListener}>Report Button</button>

     {/* On div wrapping Grid a) specify theme CSS Class Class and b) sets Grid size */}
     <div className="ag-theme-alpine" style={{width: 1100, height: 500}}>

       <AgGridReact
           ref={gridRef} // Ref for accessing Grid's API

           rowData={rowData} // Row Data for Rows

           columnDefs={columnDefs} // Column Defs for Columns
           
           defaultColDef={defaultColDef} // Default Column Properties

           animateRows={true} // Optional - set to 'true' to have rows animate when sorted
           rowSelection='multiple' // Options - allows click selection of rows

           onCellClicked={cellClickedListener} // Optional - registering for Grid Event
           />
     </div>
   </div>
 );

 };

 
export default AppPage
