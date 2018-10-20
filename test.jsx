const styles = {
  main: {
    margin: 15,
    lineHeight: 1.4,
    fontFamily: 'Impact',
    fontSize: '24pt',
    textTransform: 'lowercase',
    textAlign: 'center'
  },
  description: {
    fontFamily: 'Helvetica Neue',
    fontSize: '10pt',
    color: '#333333',
    fontWeight: 'light',
    textAlign: 'center',
    marginTop: '-30px',
    marginBottom: '30px'
  },
  code: {
    fontFamily: 'Courier',
    fontSize: '8pt',
    fontWeight: 'light',
    color: 'gray',
    fontStyle: 'italic',
    textAlign: 'left',
    marginLeft: '120px'
  },
  body: {
    fontFamily: 'Helvetica Neue',
    fontSize: '12pt',
    textAlign: 'left',
    marginLeft: '100px'
  },
};

const ColoredLine = ({ color }) => (
    <hr
        style={{
            color: color,
            backgroundColor: color,
            height: 1,
            width: '90%'
        }}
    />
);



ReactDOM.render(
    <div style={styles.main}>
  <p>This is the title of some blog entry.</p>
    <p style={styles.description}>The bottom of the barrel.</p>
  <p style={ styles.body }>Custom Font from first google style.</p>
  <p style={ styles.code }>Custom Font from second google style.</p>
    </div>
,
  document.getElementById('root')
);
