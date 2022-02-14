//
//  main.swift
//  220213
//
//  Created by 김재희 on 2022/02/13.
//

import Foundation

class Solution {
    func plusOne(_ digits: [Int]) -> [Int] {
        var plusOne = 0
        let count = digits.count
        for (i, num) in digits.enumerated() {
            plusOne += NSDecimalNumber(decimal: pow(10, count - 1 - i)).intValue * num
        }
        plusOne += 1
        let result = "\(plusOne)".compactMap { $0.wholeNumberValue}
        return result
    }
}

