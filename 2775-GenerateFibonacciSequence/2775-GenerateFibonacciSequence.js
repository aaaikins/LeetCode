// Last updated: 12/18/2025, 1:50:12 PM
/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
    let a = 0;
    let b = 1;
    // // let c;
    // yield a;

    // yield b;

    while (true){
        
        yield a;
        [a, b] = [b, a + b];
    }
};


/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */