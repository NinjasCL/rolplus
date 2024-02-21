const hideItems = (items) => {
    items.forEach(el => {
       el.classList.add("hidden");
    });
};

const showItems = (items) => {
    items.forEach(el => {
        el.classList.remove("hidden");
    });
};

const setEnglish = () => {
    const english = Array.from(document.getElementsByClassName("english"));
    showItems(english);

    const spanish = Array.from(document.getElementsByClassName("spanish"));
    hideItems(spanish);

    document.getElementById("button-lang-english").classList.add("is-primary");
    document.getElementById("button-lang-spanish").classList.remove("is-primary");

    window.language = "english";
};

const setSpanish = () => {
    const english = Array.from(document.getElementsByClassName("english"));
    hideItems(english);

    const spanish = Array.from(document.getElementsByClassName("spanish"));
    showItems(spanish);

    document.getElementById("button-lang-english").classList.remove("is-primary");
    document.getElementById("button-lang-spanish").classList.add("is-primary");

    window.language = "spanish";
};