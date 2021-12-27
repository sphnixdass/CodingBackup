const fun = require('./jScript');

test('Test the CalulateMarks function', ()=> {
    expect(fun.calculateMarks()).toEqual([{"Class": 3, "Marks": [50, 80, 40], "Names": "Caleb"}, {"Class": 4, "Marks": [80, 80, 80], "Names": "Suresh"}]);
});
