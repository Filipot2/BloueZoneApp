import {Calendar} from "@fullcalendar/core";
import dayGridPlugin from "@fullcalendar/daygrid"
import timeGridPlugin from  "@fullcalendar/timegrid"
import tippy from "tippy.js"
import 'tippy.js/dist/tippy.css'
import 'tippy.js/themes/light.css'



// javascript for the calendar includes fetching events
document.addEventListener("DOMContentLoaded", function () {

    const calendarEl = document.getElementById("calendar");
    const tooltipMap = new WeakMap
    const calendar = new Calendar(calendarEl,
        {
            plugins: [dayGridPlugin, timeGridPlugin],

            initialView: "timeGridDay",

            headerToolbar: {
                left: 'prev,next today',
                center: 'title',
                right: 'dayGridMonth, timeGridWeek, timeGridDay'
            },

            timeZone: 'UTC',

            eventClick: function (info){

                alert(info.event.title)

            },

            eventMouseEnter: function (info){

                if (tooltipMap.has('{info.el}')){
                    tooltipMap.get(info.el).destroy()
                }

                const instance = tippy(info.el, {
                    content: info.event.title,
                    placement:'top-start',
                    arrow:true,
                    animation: 'scale-extreme'
                });

                instance.show();
                tooltipMap.set(info.el, instance);

            },

            events: function (response, successCallback, errorCallback) {
                fetch('fetch')
                    .then(response => response.json())
                    .then(data => {
                        const events = data.data.map(lecture => ({
                            title: lecture.name_lecture,
                            start: lecture.start_time,
                            end: lecture.end_time
                        }));
                        successCallback(events)
                        console.log('fetched success');
                    })

                    .catch(error => {
                        console.log('Error Fetching', error);
                        errorCallback(error)
                    });
            }
        });
    calendar.render();
});




document.addEventListener("DOMContentLoaded", function (){
    document.getElementById('jokeButton').addEventListener('click', get_joke)
});

document.addEventListener("DOMContentLoaded", function (){
    document.getElementById('hiddJokeButton').addEventListener('click', hidd_joke)
});


function hidd_joke(){

    const container = document.getElementById('jokeContainer');

    if (container && container.classList.contains('visible'))  {

            container.classList.remove('visible');
            container.classList.add('hidden');

    }
    else {
        console.error('container was not found');
    }
}


async function get_joke() {

    const container = document.getElementById('jokeContainer')
    const setup = document.getElementById("jokeSetup")
    const punchline = document.getElementById('jokePunchline')


try {
    const response = await fetch("https://official-joke-api.appspot.com/random_joke");
    const Data = await response.json();

    setup.textContent = Data.setup;
    punchline.textContent = Data.punchline;

    container.classList.remove('hidden');
    container.classList.add(('visible'));
}
catch (error){
        console.error('Error fetching joke:', error);
}
}

