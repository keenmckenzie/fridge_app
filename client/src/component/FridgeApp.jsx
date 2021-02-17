import React, { Component } from 'react';
import {
    BrowserRouter as Router,
    Switch,
    Route
  } from "react-router-dom";

import ListItemsComponent from './ListItemsComponent'
import ItemComponent from './ItemComponent'

class FridgeApp extends Component {
    render() {
        return (
            <Router>
                <>
                    <h1>McKenzie House</h1>
                    <Switch>
                        <Route path="/" exact component={ListItemsComponent} />
                        <Route path="/items" exact component={ListItemsComponent} />
                        <Route path="/items/:id" component={ItemComponent} />
                    </Switch>
                </>
            </Router>
        )
    }
}

export default FridgeApp