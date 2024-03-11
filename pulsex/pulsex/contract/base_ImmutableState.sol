// SPDX-License-Identifier: GPL-2.0-or-later
pragma solidity =0.7.6;

import '../interfaces/IImmutableState.sol';

/// @title Immutable state
/// @notice Immutable state used by the swap router
abstract contract ImmutableState is IImmutableState {
    /// @inheritdoc IImmutableState
    address public immutable override factoryV1;
    /// @inheritdoc IImmutableState
    address public immutable override factoryV2;
    /// @inheritdoc IImmutableState
    address public immutable override WETH9;

    constructor(address _factoryV1, address _factoryV2, address _WETH9) {
        factoryV1 = _factoryV1;
        factoryV2 = _factoryV2;
        WETH9 = _WETH9;
    }
}
