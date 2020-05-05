import React, { Component } from 'react';
import { Formik, Form, Field, ErrorMessage} from 'formik';
import ItemDataService from '../service/ItemDataService';
import moment from 'moment';


class ItemComponent extends Component {

    constructor(props) {
        super(props)

        this.state = {
            id: this.props.match.params.id,
            name: '',
            createdAt: '',
            expirationDate: '',
        }
        this.retrieveItem = this.retrieveItem.bind(this)
        this.onSubmit = this.onSubmit.bind(this)
        this.validate = this.validate.bind(this)

    }

    componentDidMount() {

        console.log(this.state.id)

        if (this.state.id == -1) {
          return
        }

        this.retrieveItem(this.state.id)
        /*
        ItemDataService.retrieveItem(this.state.id)
            .then(response => this.setState({
                name: response.data.name
            }))
            */
    
    }

    retrieveItem(id) {
      ItemDataService.retrieveItem(id)
      .then(response => 
        {
        this.setState({
          name: response.data.name,
          count: response.data.count,
          daysToExpiration: response.data.daysToExpiration,
          expirationDate: moment(response.data.expirationDate).format('YYYY-MM-DD')
      });
      console.log(response.data)
    })
    }

    onSubmit(values) {
      let item = {
        id: this.state.id,
        name: values.name,
        count: values.count,
        daysToExpiration: values.daysToExpiration,
        expirationDate: values.expirationDate,
        targetDate: values.targetDate
    }

    if (this.state.id == -1) {
        ItemDataService.createItem(item)
            .then(() => this.props.history.push('/items'))
    } else {
        ItemDataService.updateItem(this.state.id, item)
            .then(() => this.props.history.push('/items'))
    }

    console.log(values);
    }

    validate(values) {
      let errors = {}
      if (!values.name) {
          errors.name= 'Enter a Name'
      } else if (values.name.length < 2) {
          errors.name = 'Enter atleast 2 Characters in Name'
      }
  
      return errors
    }

    render() {

        let { count, name, id, expirationDate, daysToExpiration } = this.state

        return (
          <div>
              <h3>Item</h3>
              <div className="container">
                  <Formik
                      initialValues={{ id, name, count, daysToExpiration, expirationDate }}
                      onSubmit={this.onSubmit}
                      validateOnChange={false}
                      validateOnBlur={false}
                      validate={this.validate}
                      enableReinitialize
                  >
                      {
                          (props) => (
                              <Form>
                                <ErrorMessage name="name" component="div"
    className="alert alert-warning" />
                                  <fieldset className="form-group">
                                      <label>Id</label>
                                      <Field className="form-control" type="text" name="id" disabled />
                                  </fieldset>
                                  <fieldset className="form-group">
                                      <label>Name</label>
                                      <Field className="form-control" type="text" name="name" />
                                  </fieldset>
                                  <fieldset className="form-group">
                                    <label>Count</label>
                                    <Field className="form-control" type="number" name="count" />
                                  </fieldset>
                                  <fieldset className="form-group">
                                    <label>Days to Expire</label>
                                    <Field className="form-control" type="number" name="daysToExpiration" />
                                  </fieldset>
                                  <fieldset className="form-group">
                                    <label>Expires (Leave blank for new item)</label>
                                    <Field className="form-control" type="date" name="expirationDate"/>
                                  </fieldset>
                                  <button className="btn btn-success" type="submit">Save</button>
                              </Form>
                          )
                      }
                  </Formik>
  
              </div>
          </div>
      )
    }
}

export default ItemComponent