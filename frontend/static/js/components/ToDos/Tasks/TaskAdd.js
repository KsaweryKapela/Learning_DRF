import React, {useState} from 'react'
import axios from "axios";
import formOnClick from "../formOnClick";
import getCookie from '../../csrfToken/getCookie'


export default function TaskAdd(PL_ID) {
    const [values, setValues] = useState({
        PL: 'Add new task'
    });

    const csrftoken = getCookie('csrftoken');

    const handleInputChange = (event) => setValues({values, PL: event.target.value})

    const handleKeypress = (event) => {
    if (event.keyCode === 13) {

      axios({
             method: "post",
             url: "http://127.0.0.1:8000/edit-todos/",
             data: {language: PL_ID.PL_ID,
                    name: values.PL,
                    description: 'Description of ' + values.PL,
                    done: false},
             headers: {
                       'Accept': 'application/json',
                       'Content-Type': 'application/json',
                       'X-CSRFToken': csrftoken
                       }})

      setValues({values, PL: ''})
      window.location.reload();
    }}

    return (
        <div>
            <hr/>
            <input value={values.PL}
                   onChange={handleInputChange}
                   onKeyDown={handleKeypress}
                   onClick={(e) => formOnClick(e)}
            />
        </div>
    )
}