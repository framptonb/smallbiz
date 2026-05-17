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

document.addEventListener("click", function (event) {
    const aboutVideoTrigger = event.target.closest(".about-video-trigger");

    if (aboutVideoTrigger) {
        const modal = document.getElementById("about-video-modal");
        const video = modal ? modal.querySelector(".about-video-player") : null;

        if (modal) {
            modal.classList.add("is-open");
            modal.setAttribute("aria-hidden", "false");
            document.body.classList.add("modal-open");

            if (video) {
                video.currentTime = 0;
                video.play().catch(function () {
                    // Some browsers may block autoplay until the user interacts with controls.
                });
            }
        }

        return;
    }

    const aboutVideoClose = event.target.closest(".about-video-close");

    if (aboutVideoClose) {
        const modal = aboutVideoClose.closest(".about-video-modal");
        const video = modal ? modal.querySelector(".about-video-player") : null;

        if (video) {
            video.pause();
        }

        if (modal) {
            modal.classList.remove("is-open");
            modal.setAttribute("aria-hidden", "true");
            document.body.classList.remove("modal-open");
        }

        return;
    }

    const aboutVideoModal = event.target.closest(".about-video-modal");

    if (aboutVideoModal && event.target === aboutVideoModal) {
        const video = aboutVideoModal.querySelector(".about-video-player");

        if (video) {
            video.pause();
        }

        aboutVideoModal.classList.remove("is-open");
        aboutVideoModal.setAttribute("aria-hidden", "true");
        document.body.classList.remove("modal-open");
    }
});

document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") {
        const modal = document.querySelector(".about-video-modal.is-open");

        if (modal) {
            const video = modal.querySelector(".about-video-player");

            if (video) {
                video.pause();
            }

            modal.classList.remove("is-open");
            modal.setAttribute("aria-hidden", "true");
            document.body.classList.remove("modal-open");
        }
    }
});