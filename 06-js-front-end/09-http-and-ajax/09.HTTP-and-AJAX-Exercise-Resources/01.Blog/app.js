function attachEvents() {
    const baseURL = "http://localhost:3030/jsonstore/blog";
    const postsResource = "/posts";
    const commentsResource = "/comments";

    // HTML Elements 
    const loadButtonElement = document.getElementById('btnLoadPosts');
    const selectElement = document.getElementById('posts');
    const viewButtonElement = document.getElementById('btnViewPost');
    const titleElement = document.getElementById('post-title');
    const postElement = document.getElementById('post-body');
    const commentsULElement = document.getElementById('post-comments');

    loadButtonElement.addEventListener('click', () => {
        fetch(baseURL + postsResource)
            .then(response => response.json())
            .then(data => {
                for (const key in data) {
                    // console.log(key);
                    // console.log(data[key]);
                    const optionElement = document.createElement('option');
                    optionElement.value = key;
                    optionElement.textContent = data[key].title;
                    selectElement.appendChild(optionElement);
                }
            })
        
    })

    viewButtonElement.addEventListener('click', () => {
        const selectedValue = selectElement.value;
        // Post title and body
        fetch(baseURL + postsResource + "/" + selectedValue)
            .then(response => response.json())
            .then(post => {
                titleElement.textContent = post.title;
                postElement.textContent = post.body;
            })
        // Comments
        fetch(baseURL + commentsResource)
            .then(response => response.json())
            .then(data => {
                const comments = Object.values(data).filter(obj => obj['postId'] === selectedValue);
                comments.forEach(obj => {
                    const commentText = obj.text;
                    const listElement = document.createElement('li');
                    listElement.textContent = commentText;
                    commentsULElement.appendChild(listElement);
                })
            })
    })
}

attachEvents();