console.log("smallbiz_site.js loaded");

document.addEventListener("click", function (event) {
    const readMoreButton = event.target.closest("[data-modal-target]");

    if (readMoreButton) {
        const modalId = readMoreButton.getAttribute("data-modal-target");
        const modal = document.getElementById(modalId);

        if (modal) {
            modal.classList.add("is-open");
            document.body.classList.add("modal-open");
        }

        return;
    }

    const closeButton = event.target.closest(".studywork-modal-close");

    if (closeButton) {
        const modal = closeButton.closest(".studywork-program-modal");

        if (modal) {
            modal.classList.remove("is-open");
            document.body.classList.remove("modal-open");
        }

        return;
    }

    const modal = event.target.closest(".studywork-program-modal");

    if (modal && event.target === modal) {
        modal.classList.remove("is-open");
        document.body.classList.remove("modal-open");
    }
});

document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") {
        const openModal = document.querySelector(".studywork-program-modal.is-open");

        if (openModal) {
            openModal.classList.remove("is-open");
            document.body.classList.remove("modal-open");
        }
    }
});