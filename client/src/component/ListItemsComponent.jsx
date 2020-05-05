import React, { Component } from 'react';
import ItemDataService from '../service/ItemDataService'
import moment from 'moment';

class ListItemsComponent extends Component {

    constructor(props) {
        super(props)
        this.state = {
            items: [],
            message: null
        }
        this.refreshItems = this.refreshItems.bind(this)
        this.deleteItemClicked = this.deleteItemClicked.bind(this)
        this.updateItemClicked = this.updateItemClicked.bind(this)
        this.addItemClicked = this.addItemClicked.bind(this)
    }

    componentDidMount() {
        this.refreshItems();
    }

    refreshItems() {
        ItemDataService.retrieveAllItems()//HARDCODED
            .then(
                response => {
                    console.log(response.data);
                    this.setState({ items: response.data })
                    console.log(this.state)
                }
            )
    }

    updateItemClicked(id) {
        console.log('update ' + id)
        this.props.history.push(`/items/${id}`)
    }

    deleteItemClicked(id, name) {
        ItemDataService.deleteItem(id)
            .then(
                response => {
                    this.setState({ message: `Delete of ${name} Successful` })
                    this.refreshItems()
                }
            )
    
    }

    addItemClicked() {
        this.props.history.push(`/items/-1`)
    }

    render() {
        return (
            <div className="container">
                <h3>All Items</h3>
                {this.state.message && <div class="alert alert-success">{this.state.message}</div>}
                <div className="container">
                    <table className="table">
                        <thead>
                            <tr>
                                <th>Name</th>
                                <th>Count</th>
                                <th>Date Added</th>
                                <th>Expiration Date</th>
                                <th>Update</th>
                                <th>Remove Item</th>
                            </tr>
                        </thead>
                        <tbody>
                        {
                                this.state.items.map(
                                    item =>
                                        <tr key={item.id}>
                                            <td>{item.name}</td>
                                            <td>{item.count}</td>
                                            <td>{moment(item.createdAt).format('MM/DD/YYYY')}</td>
                                            <td>{moment(item.expirationDate).format('MM/DD/YYYY')}</td>
                                            <td><button className="btn btn-success" onClick={() => this.updateItemClicked(item.id)}>Update</button></td>
                                            <td><button className="btn btn-warning" onClick={() => this.deleteItemClicked(item.id, item.name)}>Delete</button></td>
                                        </tr>
                                )
                            }
                        </tbody>
                    </table>
                </div>
                <div className="row">
                    <button className="btn btn-success" onClick={this.addItemClicked}>Add</button>
                </div>
            </div>
        )
    }
    
}

export default ListItemsComponent