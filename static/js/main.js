const formButton = document.querySelector('form button');

formButton.addEventListener('click', async (event) => {
    event.preventDefault();

    let question = document.querySelector('input').value;
    console.log(question)

    listoftags = await receiveTags(question);
    displayTags(listoftags);

    
})

async function receiveTags(question) {

    const fullData = {"question": question};

    const response = await fetch('/suggest', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'        },
        body: JSON.stringify(fullData)
    });

    const responseData = await response.json();

    console.log(response)
    console.log(responseData)
    console.log(responseData.tags)
    console.log(typeof responseData.tags)
    console.log(responseData.tags[0])


    return responseData.tags; 

}

function displayTags(tags) {

    console.log(typeof tags)
    console.log(tags)

    const form = document.querySelector('form');
    const suggestedTags = 'Tags suggérés: ' + tags.join(', ');
    const tagsHTMLElement = document.createElement('p');
    tagsHTMLElement.textContent = suggestedTags;
    form.appendChild(tagsHTMLElement);

};

