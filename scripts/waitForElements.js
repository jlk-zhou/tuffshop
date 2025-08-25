// Script that tells playwright to wait until desired number of element is rendered. 
// This function takes two parameters: product card "selector" and "countSelector". 
// Vibe-coded using Microsoft Copilot. 

async function waitForCount(selector, count, timeout = 20000) {
    // // Extract the desired count from the page
    // const targetCount = parseInt(document.querySelector(countSelector).innerText);

    // // Catch error in case count can't be retrieved
    // if (!targetCount || isNaN(targetCount)) {
    //     console.warn("Could not determine target count from page.");
    //     return;
    // }

    const start = Date.now();

    // Stay in loop as long as some products are not loaded
    while (document.querySelectorAll(selector).length < count) {

        // Refresh every 0.5 seconds
        await new Promise(resolve => setTimeout(resolve, 500));

        // Give up if time out
        if (Date.now() - start > timeout) {
            console.warn(`Timeout: Only ${document.querySelectorAll(selector).length} elements found.`);
            break;
        }
    }
}

// Call the function 
waitForCount(".product-item-info", 201);