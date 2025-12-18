// Last updated: 12/18/2025, 1:50:19 PM
/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
    return new Promise((resolve) => {
        setTimeout(
            resolve, millis)
    });
    
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */