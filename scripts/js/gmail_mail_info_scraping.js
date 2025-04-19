function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

thetext = ""
async function processEmails() {
    const rows = document.querySelectorAll("tr.zA.yO");

    for (const row of rows) {
        row.click();
        await delay(1000); // wait 1 second

        const targetSpans = [...document.querySelectorAll("span")]
            .filter(span => span.textContent.trim().startsWith("to"));

        const emailSpans = targetSpans.flatMap(parent =>
            [...parent.querySelectorAll("span")]
                .filter(child => child.hasAttribute("email"))
        );

        email = emailSpans.map(e => e.getAttribute("email")).filter(Boolean);
        
        from = [...new Set(
          [...row.querySelectorAll("span.yP")].map(e => e.getAttribute("email"))
        )];
        thetext += `{"from":"${from}","to":"${email}"}`;
        thetext += "\n";
    }
    console.log(thetext);
}


processEmails();