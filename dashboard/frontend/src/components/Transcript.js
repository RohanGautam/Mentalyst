import React from "react";
import { withStyles } from "@material-ui/core/styles";
import {
  Paper,
  Typography,
  Grid,
  Button,
  Dialog,
  DialogTitle,
  DialogActions,
  DialogContent,
  DialogContentText
} from "@material-ui/core";

const styles = theme => ({
  button: {
    margin: theme.spacing.unit
  },
  input: {
    display: "none"
  },
  chip: {
    margin: theme.spacing.unit,
    height: 50,
    fontSize: 30
  }
});

class Transcript extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      text: "This is the selected text",
      open: false,
      facts: ""
    };
  }

  handleClickOpen = () => {
    this.setState({ open: true });
    this.getFacts(this.state.text);
    console.log(this.state.text);
  };

  handleClose = () => {
    this.setState({ open: false });
  };

  getFacts = textToSend => {
    const data = new FormData();
    data.append("transcript", textToSend);

    return fetch("http://localhost:8000/transcript", {
      method: "POST",
      body: data
    }).then(response => {
      response.json().then(response => {
        console.log(response.data);

        var stringified = JSON.stringify(response.data);
        var parsedObj = JSON.parse(stringified);
        this.setState({
          facts: parsedObj
        });
      });
    });
  };

  getSelectionText = () => {
    var text = "";
    if (window.getSelection) {
      text = window.getSelection().toString();
    } else if (document.selection && document.selection.type !== "Control") {
      text = document.selection.createRange().text;
    }
    this.setState({
      text: text
    });
  };

  componentDidMount() {
    this.interval = setInterval(() => {
      this.getSelectionText();
    }, 1000);
  }

  render() {
    const { classes } = this.props;

    var arr = [];

    Object.keys(this.state.facts).forEach(key => {
      arr.push(key);
    });

    var factCards = (
      <Paper
        style={{ maxHeight: 2000, overflow: "auto", width: 600, margin: 10 }}
        elevation={1}
      >
        <Grid
          container
          direction="column"
          alignContent="center"
          alignItems="center"
        >
          <Grid container direction="row">
            <Grid item>
              <DialogContentText>Claim:</DialogContentText>
              <DialogContentText>{this.state.facts}</DialogContentText>
            </Grid>
          </Grid>
        </Grid>
      </Paper>
    );

    return (
      <div>
        <Paper
          style={{ maxHeight: 2000, overflow: "auto", width: 600, margin: 10 }}
          elevation={1}
        >
          <Grid
            container
            direction="row"
            alignContent="center"
            alignItems="center"
          >
            <Typography variant="h5" component="h3">
              {this.state.text}
            </Typography>
            <Button
              color="primary"
              variant="outlined"
              className={classes.button}
              onClick={this.handleClickOpen}
            >
              Fact Check
            </Button>
          </Grid>
        </Paper>
        <Paper
          style={{ maxHeight: 500, overflow: "auto", width: 600, margin: 10 }}
          elevation={1}
        >
          <Typography variant="h5" component="h3">
            In Chicago, which has the toughest gun laws in the United States,
            probably you could say by far, they have more gun violence than any
            other city. Firearms are cheaper in Indiana. There's less detection,
            there are less requirements in Indiana and that's why we are seeing
            this steady flow and large volume of crime originating better.
            Chicago police superintendent Gary McArthur says its's a big reason
            he says he's confiscated more than 3000 guns in Chicago that have
            come from Indiana. 16,500-plus ICE last week, endorsed me. First
            time they've ever endorsed a candidate. ICE spokeswoman Sarah
            Rodriguez stated Federal agencies are prohibited from engaging in
            partison political activity including the endorsement of any
            candidate for office.
          </Typography>
        </Paper>
        <Dialog
          open={this.state.open}
          onClose={this.handleClose}
          aria-labelledby="alert-dialog-title"
          aria-describedby="alert-dialog-description"
          fullWidth={true}
          maxWidth={"md"}
        >
          <DialogTitle id="alert-dialog-title">
            Some results regarding your fact check query:
          </DialogTitle>
          <DialogContent>
            <Typography variant="h5">Claim:</Typography>
            <Typography variant="h5">{this.state.facts}</Typography>
          </DialogContent>
          <DialogActions>
            <Button onClick={this.handleClose} color="primary">
              OK
            </Button>
          </DialogActions>
        </Dialog>
      </div>
    );
  }
}

export default withStyles(styles)(Transcript);
