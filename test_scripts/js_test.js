// test_scripts/js_test.js
const { performance } = require('perf_hooks');
const process = require('process');

function chudnovsky(iterations) {
    // Using BigInt for precise calculations
    const C = BigInt(426880) * BigInt(Math.floor(Math.sqrt(10005) * 1e15));
    let L = BigInt(13591409);
    let X = BigInt(1);
    let M = BigInt(1);
    let K = BigInt(6);
    let S = L;
    
    for (let i = 1; i < iterations; i++) {
        M = ((K ** BigInt(3) - BigInt(16) * K) * M) / BigInt(i ** 3);
        L += BigInt(545140134);
        X *= BigInt(-262537412640768000);
        K += BigInt(12);
        S += (M * L) / X;
    }
    
    // Convert back to number with proper scaling
    return Number(C) / Number(S) / 1e15;
}

function getMemoryUsage() {
    const used = process.memoryUsage();
    return used.heapUsed / 1024 / 1024; // Convert to MB
}

function runTest(iterations = 1000, runs = 100) {
    const startTime = performance.now();
    let pi;
    
    for (let i = 0; i < runs; i++) {
        pi = chudnovsky(iterations);
    }
    
    const endTime = performance.now();
    const duration = (endTime - startTime) / 1000; // Convert to seconds
    
    return {
        duration,
        pi_value: pi,
        memory_used: getMemoryUsage()
    };
}

// Run the test and output results as JSON
const result = runTest();
console.log(JSON.stringify(result));